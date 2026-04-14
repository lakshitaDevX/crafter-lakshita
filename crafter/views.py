from django.shortcuts import render, redirect
from .models import Artworks, Contact, Gallery, Purchase
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


def profile(request):
    purchases = Purchase.objects.filter(user=request.user)

    return render(request, "profile.html", {"purchases": purchases})


def gallery(request):
    arts = Gallery.objects.all()
    return render(request, "gallery.html", {"arts": arts})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)

        send_mail(
            subject="Thanks for contacting us",
            message="Thank you for your message. We will contact you soon.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Contact submitted successfully")
        return redirect("contact")

    return render(request, "contact.html")


def artwork_list(request):
    artworks = Artworks.objects.all()
    return render(request, "buyart.html", {"artworks": artworks})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successfully")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def buy(request, artwork_id):
    artwork = Artworks.objects.get(id=artwork_id)
    if request.method == "POST":
        Purchase.objects.create(user=request.user, artwork=artwork, price=artwork.price)
        return redirect("profile")
    return render(request, "buy.html", {"artwork": artwork})


def sign(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("sign")

        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "sign.html")
