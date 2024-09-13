from django.contrib import admin
from django.urls import path, include
from restapi import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.Userviewset)
router.register(r'groups', views.Groupviewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
