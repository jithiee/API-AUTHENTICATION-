
from django.contrib import admin
from django.urls import path,include
from api import views



from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentApiView.as_view(),),
    path('studentapi/<int:pk>/',views.StudentApiView.as_view(),),
]
