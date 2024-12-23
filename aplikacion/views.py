from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {"items":items, "categories":categories}
    return render(request, "home.html", context)

def about(request):
    categories = Category.objects.all()
    context={"categories":categories}
    return render(request, "about.html", context)

def contact(request):
    categories = Category.objects.all()
    context={"categories":categories}
    if request.method == "POST":
        firstname = request.POST["first-name"]
        lastname = request.POST["mbiemri"]
        email = request.POST["email"]
        koment = request.POST["koment"]
        if firstname !="" and lastname !="" and email !="" and koment!="":
            Contact(contact_name=firstname, contact_surname = lastname,
                    contact_email=email, contact_comment=koment).save()
            messages.success(request, "Messages Sent. Thank You")
        else:
            messages.error(request, "Messages not sent")
    return render(request, "contact.html", context)

def detailcategory(request, id):
    categories = Category.objects.all()
    categoryDetails = Category.objects.get(pk=id)
    categoryItem = Item.objects.filter(item_category=categoryDetails)
    context ={"categoryDetail":categoryDetails, 
              "categories":categories,
              "categoryItem":categoryItem}
    return render(request, "detailCategory.html",context)
