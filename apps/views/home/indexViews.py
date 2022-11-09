from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection

def IndexViews(request):
    return render(request, 'home/index.html')