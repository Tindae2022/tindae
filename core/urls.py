from django.urls import path
from .views import (IndexTemplateView, PostDetailView,
                  CommentCreateView, MessageCreateView,
CategoryTagListView, FilteredPostListView

                    )

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),

    path('all_post/', CategoryTagListView.as_view(), name='all_post'),
    path('category/<int:category_id>/', FilteredPostListView.as_view(), name='category_post_list_by_id'),
    path('tag/<int:tag_id>/', FilteredPostListView.as_view(), name='tag_post_list_by_id'),
    path('all_post/<int:pk>/', PostDetailView.as_view(), name='post_details'),

    # path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_post'),


    path('post/<int:post_id>/comment/', CommentCreateView.as_view(), name='add_comment'),

    path('send-message', MessageCreateView.as_view(), name='send_message'),




]

