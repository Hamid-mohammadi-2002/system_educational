from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user_is_registered = User.objects.filter(email=form.cleaned_data['email']).exists()

            if user_is_registered:
                # If we have user with this username in database
                messages.error(request, 'We have user with this email')
                return render(request, 'accounts/sign_up.html', {'form': form})

            # # If user is not registered, register user and redirect to sign in view
            # new_user = User(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
            #                 username=form.cleaned_data['username'],
            #                 email=form.cleaned_data['email'])
            # new_user.set_password(form.cleaned_data['password'])
            # new_user.save()
            return redirect('accounts:sign_in')

    # If user get url
    form = RegisterForm()
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_for_login = authenticate(request, email=email, password=password)

            # If user  successfully authenticated redirect user to register student url
            if user_for_login is not None:

                login(request, user_for_login)
                return redirect('university:registere_students')

            else:
                # If user doesnt authenticated
                messages.error(request, 'Incorrect email or password')
                return render(request, 'accounts/sign_in.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/sign_in.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('university:index')
