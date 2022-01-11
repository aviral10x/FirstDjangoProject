from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developed_by = "Aviral"
    languages = [
        "JAVA",
<<<<<<< HEAD
        "C++",
=======
        "C++"",
>>>>>>> d437a416e87faa2f00de9244185251857d7399fa
        "HTML",
        "CSS",
        "JAVASCRIPT",
        "DJANGO"
        ]

    context = {
<<<<<<< HEAD
            "developer": developed_by,
            "languages": languages
=======
            developer: "developed_by",
            languages: "languages"
>>>>>>> d437a416e87faa2f00de9244185251857d7399fa
        }
    response = render(request, 'index.html', context)

    return response
