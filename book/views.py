from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_page(request):
    return HttpResponse("Hello les Boss")


def contact_page(request):
    return HttpResponse("""
    <h1 style='color:red;'> Page de contact </h1>
""")
