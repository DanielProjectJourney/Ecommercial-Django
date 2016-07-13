from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)

@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request,template,context)
