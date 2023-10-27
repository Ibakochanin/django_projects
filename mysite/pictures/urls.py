from django.urls import path
from . import views

app_name = 'pictures'
urlpatterns = [
    path('pictures/', views.picture_list, name='picture_list'),
    path('chosen_picture/<int:image_id>/', views.chosen_picture, name='chosen_picture'),
]
