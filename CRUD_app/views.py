from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from CRUD_app.models import NewUser
from CRUD_app.forms import RegisterForm, LoginForm, EditForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    blogers = NewUser.objects.all()
    return render(request, 'crud_app/home.html', {'all_blogers': blogers})


def edit_user(request, id):
    if request.method == 'POST':
        single_bloger = get_object_or_404(NewUser, id=id)
        #single_bloger = NewUser.objects.get(id=id)
        frm = EditForm(request.POST, instance=single_bloger)
        if frm.is_valid():
            frm.save()
            messages.success(
                request, "Account for {0} is created Successfully".format(single_bloger))
            return redirect('CRUD_app:home')
    else:
        single_bloger = get_object_or_404(NewUser, id=id)
        frm = EditForm(instance=single_bloger)
    return render(request, 'crud_app/editprofile.html', {'single_bloger': single_bloger, 'form': frm})


def delete_user(request, id):
    obj = get_object_or_404(NewUser, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('CRUD_app:home')
    return render(request, "crud_app/delete.html", context={'object': obj})


def create_user(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST, request.FILES)
        if fm.is_valid():
            print("form valid")
            full_name = fm.cleaned_data.get('full_name')
            image = fm.cleaned_data.get('image')
            username = fm.cleaned_data.get('user_name')
            email = fm.cleaned_data.get('email')
            password1 = fm.cleaned_data.get('password1')
            password2 = fm.cleaned_data.get('password2')

            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "Customer with this  {0} username is already exists".format(username))
                return redirect('CRUD_app:signup')
            else:
                if password1 != password2:
                    messages.error(request, "Password does not match")
                    return redirect('CRUD_app:signup')

                else:
                    password_hash = make_password(password2)
                    user = User.objects.create(
                        username=username, password=password_hash, email=email)

                    new_user = NewUser()
                    new_user.user = user
                    new_user.full_name = full_name
                    new_user.image = image
                    new_user.save()

                    messages.success(
                        request, "Account for {0} is created Successfully".format(user))
                    return redirect('CRUD_app:home')

    else:
        fm = RegisterForm()
    return render(request, 'crud_app/signUpUser.html', {'form': fm})


def sign_in(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                print('valid: ')
                user_name = form.cleaned_data['user_name']
                password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=password)
                if user:
                    login(request, user)
                    print("successfully login")
                    messages.success(request, "Logged in Successfully")
                    return redirect('CRUD_app:home')
                else:
                    print('not authenticate')
        return render(request, 'CRUD_app/login.html', {'form': form})
    else:
        return redirect('CRUD_app:home')


def sign_out(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("CRUD_app:signin")
