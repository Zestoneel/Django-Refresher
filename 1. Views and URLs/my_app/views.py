from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Konnichiwa, Japan!")

def about_me(request):
    me = "I'm Shreyash. Nice to meet you! My Goal is to settle in Japan! I love playing video games and learning new stuff!"
    return HttpResponse(me)

def hello(request, first_name):
    return HttpResponse(f"My name is {first_name}!")

def sum_2(request, num1, num2):
    return HttpResponse(num1 + num2)