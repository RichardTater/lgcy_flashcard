from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# Request -> Response
# Request handler
# Action

def say_hello(request):
    return render(request, 'hello.html', {
        'name': 'Lane',
        'gender': 'non-binary'
        })

def render_flashcards(request:HttpRequest):
    request.body
    return HttpResponse("Render questions here:")