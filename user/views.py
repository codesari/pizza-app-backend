from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from .forms import UserCreateForm,UserLoginForm
from django.contrib import messages

def register(request):

    if request.method == "POST":
        form=UserCreateForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            # ! burada kullanıcı henüz olmadığı için,form verilerini kullanıcı olarak kaydedeceğiz.
            messages.success(request, 'Registered successfully !')
            return redirect('home')

            # * user=form.save() 'in alternatifi
            # username = form.cleaned_data.get("username")
            # password = form.cleaned_data.get("password2")
            # user = authenticate(username=username, password=password)
            # login(request, user)
    else:
        # form=UserCreationForm()
        form=UserCreateForm()
    

    context={
        'form':form
    }

    return render(request,'user/register.html',context)


def loginUser(request):
    
    if request.method == "POST":
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            # ! kullanıcı zaten var olduğu için get_user ile aldık
            login(request,user)
            messages.info(request, 'Login successfully !')
            return redirect('home')
    else:
     form=UserLoginForm()

    context={
        'form':form
    }

    return render(request,'user/login.html',context)



def logoutUser(request):
    logout(request)
    messages.info(request, 'Logout successfully !')
    return redirect('home')