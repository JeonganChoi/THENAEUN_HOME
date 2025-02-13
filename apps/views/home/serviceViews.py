from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection

def ServiceViews(request):
    return render(request, 'pages/price.html')