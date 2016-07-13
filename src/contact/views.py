from django.shortcuts import render
from forms import contactForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    title = 'Context Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
        title = "Thanks for sending Email"
        confirm_message = "Thank for coming Daniel's Shop!"
        form = None

    context = {'title':title,'form':form,'confirm_message':confirm_message}
    template = 'contact.html'
    return render(request,template,context)
