from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User


def checkout(request):
    return render(request, "checkout.html")