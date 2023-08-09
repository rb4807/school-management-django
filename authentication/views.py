from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Register

def register(request):

    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        first_name = request.POST[ 'first_name']
        last_name = request.POST[ 'last_name']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/register')
    else:   
        return render(request, 'authentication/register.html')

# user_login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile', user_id=user.id)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'authentication/login.html')

@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'crud/data.html', {'user': user})

# user_logout

def user_logout(request):
    logout(request)
    return redirect('login')




