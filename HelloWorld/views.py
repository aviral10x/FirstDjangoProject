from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developed_by = "Aviral"
    languages = [
        "JAVA",
        "C++",
        "HTML",
        "CSS",
        "JAVASCRIPT",
        "DJANGO"
        ]

    context = {
            "developer": developed_by,
            "languages": languages
        }
    response = render(request, 'HelloWorld/index.html', context)

    return response

def hello(request):
    return render(request, "HelloWorld/hello.html")    
