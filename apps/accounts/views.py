from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm

def signup_view(request):
    """Handles new user registration.
    On POST, validates form, saves user, logs in, and redirects.
    On GET, displays the signup form."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    """Handles user login.
    On POST, validates credentials, logs in, and redirects (handles 'next' param).
    On GET, displays the login form."""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """Handles user logout. Logs out on POST and redirects."""
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
    # For GET requests, redirect to article list as well, or consider HttpResponseNotAllowed
    return redirect('articles:list') 