from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("contactUs/", views.contact, name="contactPage"),
    path("category/<id>", views.detailcategory, name="detailcategory"),
    # path("detail/",views.detailitem, name="detailitem"),
]