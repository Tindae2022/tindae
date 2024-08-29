from django.urls import path
from .views import IndexTemplateView, PostDetailView, PostListView, CategoryPostListView, CommentCreateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),

    path('all_post/', PostListView.as_view(), name='all_post'),

    path('all_post/<int:pk>/', PostDetailView.as_view(), name='post_details'),

    # path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_post'),

    path('category/', CategoryPostListView.as_view(), name='category_post_list'),
    path('category/<int:category_id>/', CategoryPostListView.as_view(), name='category_post_list_by_id'),

    path('post/<int:post_id>/comment/', CommentCreateView.as_view(), name='add_comment'),



]

