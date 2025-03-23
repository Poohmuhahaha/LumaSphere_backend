from django.urls import include, path
from rest_framework import routers
from articles_hub.views import ArticleViewSet, CategoryViewSet, TagViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
