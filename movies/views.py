from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages


def index(request):
    return render(request, 'movies/index.html')

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"account created for {username}")
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'movies/registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'movies/profile.html') 