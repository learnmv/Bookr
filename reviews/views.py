# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Book
from django.shortcuts import render, get_object_or_404
from .models import Book
from .utils import average_rating

def index(request):
    return render(request, "base.html")

def book_search(request):
    search_text = request.GET.get("search","")
    return render(request, "search-results.html",{"search_text":search_text})

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book':book,'book_rating':book_rating,'number_of_reviews':number_of_reviews})

    context = {
        'book_list':book_list
    }
    return render(request, 'reviews/books_list.html',context)

# def index(request):
#     name = request.GET.get("name") or "world"
#     return HttpResponse(f"Hola, {name}!")

# def index(request):
#     return render(request, "base.html")

# def index(request):
#     name = request.GET.get("name") or "world"
#     return render(request, "base.html", {"name": name})

# def search(request):
#     searched = request.GET.get("search") or "Nothing searched"
#     return render(request, "search.html", {"search": searched})

# def welcome_view(request):
#     return render(request, 'base.html')
