from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from manager.forms import UserRegisterForm, CustomAuthenticationForm


class MyPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)


class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = UserRegisterForm()
            return render(request, 'register.html', {'form': form})
        return redirect('the-main-page')

    def post(self, request):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.city = form.cleaned_data.get('city')
            user.profile.save()
            return redirect('login')
        messages.error(request, form.errors)
        return redirect('register')


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {'form': CustomAuthenticationForm()})

    def post(self, request):
        user = CustomAuthenticationForm(data=request.POST)
        if user.is_valid():
            login(request, user.get_user())
            return redirect('the-main-page')
        messages.error(request, "password or login is uncorrected")
        return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('the-main-page')
