from django.urls import include, path

from . import views


urlpatterns = [
    # path('media-monitoring/'),
    # path('counterparty-verification/'),
    # path('redactors-monitoring/'),
    # path('training/'),
    # path('ratings/'),
    # path('blog/'),
    # path('wp-content/uploads/2020/12/forma-sravneniya-sistem.pdf'),
    path('', views.main),
]
