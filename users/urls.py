from rest_framework.routers import SimpleRouter  # type: ignore

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)

urlpatterns = [] + router.urls
