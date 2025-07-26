from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),

]
# path('test-404/', views.test_404),
# path('test-500/', views.test_500),
# path('sentry-debug/', views.trigger_error),
