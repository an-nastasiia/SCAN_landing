from django.urls import path

from . import views


urlpatterns = [
    # path('media-monitoring/'),
    # path('counterparty-verification/'),
    # path('redactors-monitoring/'),
    # path('training/'),
    # path('ratings/'),
    # path('blog/'),
    # path('wp-content/uploads/2020/12/forma-sravneniya-sistem.pdf'),
    path('api/widget/addentitydata', views.ClientView.as_view(), name='api'),
    path('', views.main),
]
