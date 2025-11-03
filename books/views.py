from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
bookss = [
    {
        "title": "Alkimyogar",
        "author": "Paulo Coelho",
        "year": 1988,
        "pages": 208,
        "genre": "Roman"
    },
    {
        "title": "O‘tgan kunlar",
        "author": "Abdulla Qodiriy",
        "year": 1926,
        "pages": 350,
        "genre": "Tarixiy roman"
    },
    {
        "title": "1984",
        "author": "Jorj Oruell",
        "year": 1949,
        "pages": 328,
        "genre": "Fantastika"
    },
    {
        "title": "Usta va Margarita",
        "author": "Mixail Bulgakov",
        "year": 1967,
        "pages": 480,
        "genre": "Satirik roman"
    },
    {
        "title": "Sariq devni minib",
        "author": "Xudoyberdi To‘xtaboyev",
        "year": 1970,
        "pages": 240,
        "genre": "Bolalar adabiyoti"
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "year": 1997,
        "pages": 336,
        "genre": "Biznes / Motivatsiya"
    }
]


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request= request, template_name="home.html")



def books_view(request: HttpRequest) -> HttpResponse:
    context = {
        "bookss": bookss
    }
    return render(request= request, template_name="books.html", context= context)

def add_books_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")
        pages = request.POST.get("pages")
        genre = request.POST.get("genre")

        new_book = {
            "title": title,
            "author": author,
            "year": int(year),
            "pages": int(pages),
            "genre": genre
        }

        bookss.append(new_book)
        return render(request, "books.html", {"bookss": bookss})

    return render(request, "add_books.html")


def delete_books_view(request: HttpRequest) -> HttpResponse:
    return render(request= request, template_name="delete_books.html")

def update_books_view(request: HttpRequest) -> HttpResponse:
    return render(request= request, template_name="update_books.html")