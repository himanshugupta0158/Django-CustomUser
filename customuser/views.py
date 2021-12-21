from django.shortcuts import render
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DetailView)
from .models import NewUser
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your views here.

