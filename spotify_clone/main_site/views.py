from django.shortcuts import render

# Create your views here.

from .forms import SignUpForm


def homepage(request):
    return render(request, "main_site/homepage.html")


def premium(request):
    return render(request, "main_site/premium.html")


def download(request):
    return render(request, "main_site/download.html")


def account(request):
    return render(request, "main_site/account.html")


def signup(request):
    form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "main_site/signup.html",
                  context)


def login(request):
    return render(request, "main_site/login.html")


def support(request):
    return render(request, "main_site/support.html")