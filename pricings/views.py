
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import *
from django.views.generic.base import TemplateView
from django import forms

class PricingForm(forms.Form):

    food_type = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

class Home(FormView):
    form_class = PricingForm
    template_name = "index.html"
    success_url = "/thanks"
