from django.urls import path
from . import views

urlpatterns = [
    
    # Posts
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add-record/', views.addrecord, name='addrecord'),
    path('update/<int:id>', views.update, name='update'),
    path('update-record/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete'),

    # Categories
    path('categories', views.categories, name='categories'),
    path('categories/add/', views.categoriesadd, name='categoriesadd'),
    path('categories/add-record/', views.categoriesaddrecord, name='categoriesaddrecord'),
    path('categories/update/<int:id>', views.categoriesupdate, name='categoriesupdate'),
    path('categories/update-record/<int:id>', views.categoriesupdaterecord, name='categoriesupdaterecord'),
    path('categories/delete/<int:id>', views.categoriesdelete, name='categoriesdelete'),
]