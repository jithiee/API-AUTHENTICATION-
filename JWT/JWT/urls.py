

from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView  


router = DefaultRouter()
router.register('studentapi',views.StudentModelView,basename='studentapip')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path ('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view,name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view,name='verify_refresh'),
    path('auth/',include('rest_framework.urls',namespace='restframework')),

    
    

]