from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from todolist.forms import RegistrationForm
from todolist.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = User
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

def index(request):
    context = {'pagename': 'Главная страница'}
    return render(request, 'pages\\menu.html', context)

def registration_page(request):
    context = {'pagename': 'Страница регистрации'}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'], password=make_password(form.cleaned_data['password2']),
                        first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email'])
            user.save()
            user = User.objects.get(username='registered_user')
            user.username = "user_" + str(user.id)
            user.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    context['form'] = form

    return render(request, 'registration\\registration.html', context)

