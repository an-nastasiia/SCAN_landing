from django.urls import path

from . import views


urlpatterns = [
    path('api/widget/addentitydata', views.ClientView.as_view(), name='api'),
    path('', views.main),
]
