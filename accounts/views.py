from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
<<<<<<< HEAD
    template_name = 'registration/signup.html'
=======
    template_name = 'signup.html'
>>>>>>> 57c01331b0ff877aff74020566e5f78796f93456
