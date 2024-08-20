
from rest_framework.routers import DefaultRouter
from app.core.socios.api.views.socio_view import SocioViewSet

router = DefaultRouter()

router.register(r'socios', SocioViewSet, basename='socios')

urlpatterns = router.urls