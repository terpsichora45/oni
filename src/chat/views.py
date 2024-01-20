from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import User

# Create your views here.
class IndexView(generic.ListView):
    template_name = "chat/debug.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all()