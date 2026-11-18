from django.shortcuts import render, redirect,get_object_or_404
from . models import RegisterModel,ProductAdding,RegisterViewModel
from . forms import ProductAddingForm,RegisterViewForm,UpdateForm

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    if request.method == "POST":
        image = request.FILES.get("profile")
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        mydata =RegisterModel(
            profile = image,
            full_name = full_name,
            username = username,
            number = number,
            gender = gender,
            dob = dob,
            email = email,
            password = password
        )
        mydata.save()
        print("saved")

    return render(request,"register.html")

def dashboard(request):
    mydata = RegisterModel.objects.all()
    form = RegisterViewModel.objects.all()
    return render(request, "dashboard.html", {"mydata":mydata, "form":form})


def update(request, pk):
    data = RegisterModel.objects.get(id=pk)
    if request.method == "POST":
        if request.FILES.get("profile"):
            data.profile = request.FILES.get("profile")
        data.full_name = request.POST.get("full_name")
        data.username = request.POST.get("username")
        data.number = request.POST.get("number")
        data.gender = request.POST.get("gender")
        data.dob = request.POST.get("dob")
        data.email = request.POST.get("email")
        data.password = request.POST.get("password")

        data.save()
        print("saved")
    return render(request, "update.html",{"data":data} )


def delete(request, jk):
    data = RegisterModel.objects.get(id=jk)
    if request.method == "POST":
        data.delete()
        return redirect("dashboard")
    return render(request, "delete.html")

def login_view(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")

        data = RegisterModel(username=name, password=password)
        if data:
            return redirect("dashboard")
    return render(request, "login.html")

def product(request):
    if request.method == "POST":
        data = ProductAddingForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            print("saved")
    return render(request, "product.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterViewForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data["email"]
            subject = "Registration Successful"
            message = f"""
                    Hello {full_name},
                    Your registration has been completed successfully,
                    
                    Thank You,
                    """
            send_mail(subject,message,
                      settings.DEFAULT_FROM_EMAIL,[email],fail_silently=False)
            messages.success(request, "Registration Successful")
    else:
        form = RegisterViewForm() 
    return render(request, "register_view.html",{"form":form})

def update_list(request, jk):
    user = get_object_or_404(RegisterViewModel, id=jk)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form =UpdateForm(instance=user)

    return render(request, "update_list.html",{"data":form})