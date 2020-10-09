from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


#def home(request):
#   return render(request, 'home.html', {})

#ListView used to view all the post data 
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'cats':cats.title(), 'category_posts':category_posts})

#DetailView used to view single post data
class MovieDetailView(DetailView):
    model = Post
    template_name = 'movie_details.html'

#CreateView used to create post data
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #We  dont not any of below because we are using form
    #fields = ('title','body')
    #fields = '__all__' 
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__' 
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
    
    
    
    