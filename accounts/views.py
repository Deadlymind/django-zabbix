from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import RegisterCustomerForm

User = get_user_model()

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.save()
            messages.success(request, 'Accounted created ')
            return redirect ('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register-customer')
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request, 'accounts/register_customer.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, 'Active session ended. log in to continue')
    return redirect('login')


        

        
        


