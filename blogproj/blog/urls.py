from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name="blog-index"),
    path('post_details/<int:pk>',views.post_details, name='blog_post_details'),
    path('post_edit/<int:pk>',views.post_edit, name='blog_post_edit'),
    path('post_delete/<int:pk>',views.post_delete, name='blog-post-delete'), 

]