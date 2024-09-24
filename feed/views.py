from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView, DeleteView, FormView
from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name ="home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context
    
class PostDetailView(DeleteView):
    template_name = "detail.html"
    model = Post
  
  
class AddPostView(FormView):
   template_name = "new_post.html"
   form_class =  PostForm
   success_url = "/"
   
   def form_valid(self, form: Any) -> HttpResponse:
       new_object = Post.objects.create(
           text = form.cleaned_data['text'],
           image = form.cleaned_data['image']
       )
       return super().form_valid(form)