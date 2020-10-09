from django.urls import path
#from . import views
from .views import HomeView, MovieDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    #path('',views.home, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>',MovieDetailView.as_view(), name = "movie-detail"),
    path('add_post/',AddPostView.as_view(), name = "add_post"),
    path('add_category/',AddCategoryView.as_view(), name = "add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name = "update_post"),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name = "delete_post"),
    path('category/<str:cats>/', CategoryView, name = "category"),
]
