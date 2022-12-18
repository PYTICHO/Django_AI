from django.contrib import admin
from django.urls import path, include
from testApp.views import *
from rest_framework import routers

router = routers.DefaultRouter()  # Создаем роутер, для упрощенного управления API
# Регистрируем(продолжение url, viewset из views.py) он создаст url (router.urls)
router.register(r'book', BookViewSet)


# router2 = routers.DefaultRouter()
# router2.register(r'tovar', TovarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/tovar/", TovarApiView.as_view()),
    # Авторизация пользователя для API   .../login
    path('api/v1/drf-auth/', include("rest_framework.urls"))
]
