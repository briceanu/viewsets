from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BlogViews

router = DefaultRouter()

router.register(r'blog',BlogViews,basename='blog' )

urlpatterns = [
    path('', include(router.urls)),
    # path('blog/list/', BlogViews.as_view({'get': 'list'}), name='blog-list'),
    # path('blog/create/', BlogViews.as_view({'post': 'create'}), name='blog-create'),
    # path('blog/<str:pk>/', BlogViews.as_view({'get': 'retrieve'}), name='blog-detail'),
    # path('blog/update/<uuid:pk>', BlogViews.as_view({'put': 'update'}), name='blog-update'),
    # path('blog/partial-update/<uuid:pk>/', BlogViews.as_view({'patch': 'partial_update'}), name='blog-partial-update'),
    # path('blog/remove/<uuid:pk>/', BlogViews.as_view({'delete': 'destroy'}), name='blog-remove'),
]