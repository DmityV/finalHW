from rest_framework import routers

from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path

from smallblog.views import CommentViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
]
