from rest_framework.routers import DefaultRouter
from apps.posts.views import PostAPiView

router = DefaultRouter()
router.register('',PostAPiView,'api_posts')

urlpatterns = router.urls       