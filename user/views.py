from django.shortcuts import render, redirect
from .forms import RegestrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegestrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You will be able to log in.)')
            return redirect('blog-home')
    else:
        form = RegestrationForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def home_page(request):
    return render(request, 'blog/home.html')


def profile(request):
    return render(request, 'user/profile.html')

