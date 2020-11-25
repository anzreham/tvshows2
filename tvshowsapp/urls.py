from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.createform),
     path('shows/create', views.create),
     path('shows/<str:id>', views.showInfo),
     path('', views.allshows),
      path('shows', views.allshows),
     path('shows/edit/<str:id>', views.edit),
    path('shows/update/<str:id>', views.update),
     path('shows/destroy/<str:id>', views.destroy),


      

]

