from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("auth:log_in")
    return render(request, "sign_up.html", {"form": form})


def log_in(request):
    ctx = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("links:main")
        else:
            ctx['error'] = "Unfortunately, username or password is incorrect"
    return render(request, "log_in.html", ctx)


def log_out(request):
    logout(request)
    return redirect("links:main")

