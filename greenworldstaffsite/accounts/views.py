from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Staff
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Automatically log in the user after signup
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  # Redirect to some page after signup

    return render(request, 'registration/signup.html')

@login_required
def staff_list(request):
    staff_members = Staff.objects.all().order_by('full_name')
    return render(request, 'staff_list/staff_list.html', {'staff_list': staff_members})

def logout_view(request):
    logout(request)
    return redirect('logout_redirect')
