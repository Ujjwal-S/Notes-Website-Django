from django.shortcuts import redirect


def redirectToHome(request): # Redirect To Home Page When Some Access Signup Page
    if request.method == "GET":
        return redirect('/')