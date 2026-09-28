from rest_framework.routers import DefaultRouter

from .api_views import MovieViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie-api')

urlpatterns = router.urls
