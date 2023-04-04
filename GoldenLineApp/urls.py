from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from DataAnalyse.views import analyseData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('data-analyse', analyseData, name='analyse'),
]
