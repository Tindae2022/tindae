from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post, Comment, Tag, Category
from django.db.models import Count
from .forms import CommentForm
from django.urls import reverse_lazy


# Create your views here.
class IndexTemplateView(ListView):
    model = Post
    template_name = 'base.html'
    context_object_name = 'recent_posts'

    def get_queryset(self):
        return Post.objects.filter(status='Published').order_by('-publish')[:3]

    def get_context_data(self, **kwargs):
        # First, get the default context data from ListView
        context = super().get_context_data(**kwargs)

        # Add any additional context variables here if needed
        context['total_post'] = Post.objects.filter(status='Published').count()
        context['total_comment'] = Comment.objects.filter(active=True).count()

        return context


class PostListView(ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(status='Published').all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        post = self.object
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')
        context['recent_posts'] = Post.objects.filter(status='Published').order_by('-created_at')[:5]
        context['tags'] = post.tags.all()
        context['all_tags'] = Tag.objects.all()
        context['comments'] = self.object.comments.filter(active=True)
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetching posts related to this category
        context['posts'] = Post.objects.filter(category=self.object)
        return context


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/index.html'  # Create this template
    context_object_name = 'posts'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Post.objects.filter(category_id=category_id, status='Published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')
        context['selected_category'] = Category.objects.get(id=self.kwargs.get('category_id'))
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/detail.html'

    def form_valid(self, form):
        # Retrieve the post object based on the post_id passed in the URL
        post = Post.objects.get(id=self.kwargs['post_id'])
        # Associate the comment with the retrieved post
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the post detail page after a successful comment submission
        return reverse_lazy('post_details', kwargs={'pk': self.kwargs['post_id']})
