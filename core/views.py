from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login ,logout
from .forms import SignupForm
from django.contrib import messages
#Landing Page
def home(request):
    context = {}
    return render(request,'core/index.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, '! تم تسجيل الدخول بنجاح ')
            success_message = '! تم تسجيل الدخول بنجاح '
            return redirect('book:books')
        else:
            # Handle unsuccessful login
            return render(request, 'core/login.html', {'error_message': 'كلمة المرور أو اسم المستخدم غير صالح'})

    success_message=None

    return render(request, 'core/login.html')


def logout_view(request):

    logout(request)
    messages.success(request, ' ! تم تسجيل الخروج بنجاح')

    return redirect('/')


#404 not found 
def no_page(request,invalid_path):
    return render(request,'core/noPage.html')


# Coming soon view
def soon(request):
    return render(request,'core/comingSoon.html')

# Terms of use view
def termsOfUse(request):
    return render(request,'core/termsOfUse.html')
