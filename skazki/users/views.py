from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


from carts.models import Cart
from main.models import Concerts
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get("next"))

                return HttpResponseRedirect(reverse("main:news"))
    else:
        form = UserLoginForm()
    concerts = Concerts.objects.all()
    context = {"title": "Сказки Черного Города - Авторизация", "form": form, "concerts": concerts, "info_text": "Авторизация"}
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key
            
            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username}, Вы успешно зарегестрировались")
            return HttpResponseRedirect(reverse("main:news"))
    else:
        form = UserRegistrationForm()
        
    concerts = Concerts.objects.all()
    context = {"title": "Сказки Черного Города - Регистрация", "form": form, "concerts": concerts, "info_text": "Регистрация"}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Личный кабинет", 
        "form": form,
        "concerts": concerts,
        "info_text": "Личный кабинет"
        }
    return render(request, "users/profile.html", context)

def users_cart(request):
    concerts = Concerts.objects.all()
    context = {
        "concerts": concerts,
        "title": "Сказки Черного Города - Личный кабинет корзина",
        "info_text": "корзина",
    }
    return render(request, "users/users_cart.html", context=context)



@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)

    return redirect(reverse("main:news"))


