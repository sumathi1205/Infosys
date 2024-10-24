from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, username=un, password=pw)

        if user is not None:
            return redirect('/profile')
        else:
            msg = 'Error in login. Invalid username/password'
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            user = authenticate(username=un, password=pw)
            return redirect('/Login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})



def profile(request):
    return render(request, 'profile.html')




