from django.shortcuts import render

# Create your views here.

class HttpResponse:
    pass


def demo(request):
    return HttpResponse("hello world")