from django.shortcuts import render
from django.views import generic

from teamy.models import Member


class IndexView(generic.ListView):
    model = Member



