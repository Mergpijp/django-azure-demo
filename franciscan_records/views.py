# franciscan_records/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'franciscan_records/index.html', context=None)