from django.shortcuts import render


def index(request):
    context = {"title": "Home Page", "content": "Template settings"}

    return render(request, "homepage/index.html", context)
