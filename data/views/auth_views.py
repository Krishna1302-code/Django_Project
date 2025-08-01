from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import login
from ..auth_forms import CustomUserCreationForm 
from django.contrib.auth.decorators import login_required

@login_required #It will restricts access to a view only for logged-in users.
def student_dashboard(request):
    return render(request, 'auth/student_dashboard.html')

@login_required
def faculty_dashboard(request):
    return render(request, 'auth/faculty_dashboard.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, "Account created successfully!")
            return redirect('home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

 
# This is built-in login form -->AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

           
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'faculty':
                return redirect('faculty_dashboard')
            else:
                return redirect('home_page') 

        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})








# # this is custom login views 
# def login_views(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request,username=username,password=password)
    
   
#         if user is not None:
#             login(request,user)
#             messages.success(request,"logged in successfully")
#             return redirect('home_page')    
#         else:
#             messages.error(request,"Invalid username or password")

#     return render(request,'auth/login.html'   )
    

