from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    #path('',views.home, name="home"),
    #path('',HomeView.as_view(), name="home"),
    path('register/',UserRegisterView.as_view(), name="register"),

]
