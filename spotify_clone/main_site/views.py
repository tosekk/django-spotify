from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView


# Create your views here.

from .forms import SignUpForm
from .models import UserModel

def homepage(request):
    return render(request, "main_site/homepage.html")


def premium(request):
    return render(request, "main_site/premium.html")


def download(request):
    return render(request, "main_site/download.html")


def account(request):
    return render(request, "main_site/account.html")


# def signup(request):
#     if request.POST:
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             email = request.POST["user_email"]
#             conf_email = request.POST["confirm_email"]
#             if email == conf_email:
#                 user = UserModel()
#                 user.user_email = form.cleaned_data['user_email']
#                 user.user_name = form.cleaned_data['user_name']
#                 user.user_birthdate = form.cleaned_data['user_birthdate']
#                 user.user_gender = form.cleaned_data['user_gender']
#                 user.is_newsletter = form.cleaned_data['is_newsletter']
#                 user.save()
#                 print("Im here")
#                 return HttpResponseRedirect("home-page")
#             else:
#                 return render(request, "main_site/homepage.html",{
#                     "form": form,
#                 })
        
#         print("nope, here")
#         return render(request, "main_site/signup.html",{
#             "form": form,
#         })
    
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            "form": form,
        }
        return render(request, "main_site/signup.html",
                    context)
        
    def post(self, request):
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            user = UserModel()
            user.user_email = form.cleaned_data['user_email']
            user.user_name = form.cleaned_data['user_name']
            user.user_birthdate = form.cleaned_data['user_birthdate']
            user.user_gender = form.cleaned_data['user_gender']
            user.is_newsletter = form.cleaned_data['is_newsletter']
            user.save() 
            return HttpResponseRedirect(reverse("account-page"))

        return render(request, "main_site/signup.html",{
            "form": form,
        })


def login(request):
    return render(request, "main_site/login.html")


def support(request):
    return render(request, "main_site/support.html")