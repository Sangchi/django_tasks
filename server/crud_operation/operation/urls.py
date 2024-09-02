from django.urls import path
from .views import create_car_data,read_data,update_data,delete_data,create_user_data,read_user,update_user_data,delete_user_data



urlpatterns = [
    path("cars/read/",read_data),
    path("cars/create/",create_car_data),
    path("cars/update/<int:car_id>/",update_data),
    path("cars/delete/<int:car_id>/",delete_data),
    path("user/",create_user_data),
    path("user/read/",read_user),
    path("user/update/<int:booking_id>/",update_user_data),
    path("user/delete/<int:user_id>/",delete_user_data)
]
