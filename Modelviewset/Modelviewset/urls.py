
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('studentapi',views.StudentModelViewset,basename='studentapip')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    

]
