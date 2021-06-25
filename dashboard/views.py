from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Create your views here.

#
# class Postres(View):
#
#     # Especify template
#     template_name = "home.html"
#
#     # Call the file with the private keys
#     cred = credentials.Certificate('./credentials.json')
#
#     # start firebase services with the credentials included and project name
#     firebase_admin.initialize_app(cred, {
#         'databaseURL': ''
#     })


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

def index(request):
    return render(request, 'dashboard/dashboard.html')

