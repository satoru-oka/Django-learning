from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello</h1>')

def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s page</h1>')

def number_page(request, user_name, number):
    user_name = user_name.upper()
    return HttpResponse(f'<h1>page number = {user_name}\'s {number}</h1>')

# num add
def add(request, num1, num2):
    return HttpResponse(f'<h1>{num1 + num2}</h1>')

# num subtraciton
def subtraction(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{num1 - num2}</h1>')

# num division
def division(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{round(num1/num2)}</h1>')