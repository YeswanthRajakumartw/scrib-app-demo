from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm, SignUpForm

from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_type = form.cleaned_data['user_type']
            if user_type == 'volunteer':
                user.is_volunteer = True
            elif user_type == 'physically_challenged':
                user.is_physically_challenged_user = True
            user.save()
            return redirect('user-login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('exam-list')
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Check your username or password."
    else:
        form = UserLoginForm()
        error_message = None

    return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})
