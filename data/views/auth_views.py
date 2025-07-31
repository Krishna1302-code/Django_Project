from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'auth/register.html',{'form':form})   
 
# This is built-in login form -->AuthenticationForm
def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user) 
            return redirect('home_page')
        else:
            messages.error(request,"Invalid username or password")
    else:
        form=AuthenticationForm()
    return render(request,'auth/login.html',{'form':form})










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
    

