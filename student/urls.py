from django.urls import path
from . import views

urlpatterns = [
    path('insert/',views.insert,name='insert'),
    path('',views.home,name='home'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('view/<int:id>/',views.views_page,name='view')
]

