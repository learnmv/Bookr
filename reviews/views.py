# from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     name = request.GET.get("name") or "world"
#     return HttpResponse(f"Hola, {name}!")

# def index(request):
#     return render(request, "base.html")

def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})

def search(request):
    searched = request.GET.get("search") or "Nothing searched"
    return render(request, "search.html", {"search": searched})