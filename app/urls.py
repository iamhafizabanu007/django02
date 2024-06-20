from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('html1',views.html1,name="html1"),
    path('css',views.css,name="css"),
    path('tables',views.tables,name="tables"),
    path('images',views.images,name="images"),
]