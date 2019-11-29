from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return HttpResponse("Hello World! and Blog")
# Create your views here.
