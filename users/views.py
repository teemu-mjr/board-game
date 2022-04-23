from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def log_out(request):
    """Custom logout view"""
    logout(request)
    return render(request, "registration/logout.html")


def register(request):
    """Registering a new user"""
    if request.method != "POST":
        # Display plank user creation form
        form = UserCreationForm()

    else:
        # Process the form
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the new user to the website
            login(request, new_user)
            return redirect("board_games:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
