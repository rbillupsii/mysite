from django.urls import include, path
from .views import stub_view
from .views import list_view
from .views import detail_view
from .views import post_view
from .views import category_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', post_view)
router.register(r'categories', category_view)

urlpatterns = [
    path('', 
        list_view,
        name="blog_index"),
    path('posts/<int:post_id>/',
        detail_view,
        name="blog_detail"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]