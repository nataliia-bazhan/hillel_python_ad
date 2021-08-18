from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        super().form_valid(form)
        form.instance.slug = slugify(form.instance.title + str(form.instance.id))
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'slug']
    template_name = 'post_update.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostUserListView(ListView):
    model = Post
    template_name = 'post_user_list.html'

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:user_content')
    template_name = 'post_delete.html'