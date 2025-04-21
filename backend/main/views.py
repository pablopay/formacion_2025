from django.shortcuts import render
from main.controllers import get_expenses

def index(request):

    expenses = get_expenses()

    context = ('expenses' : expenses)
    return render(request, 'index.html')