from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("node_action/", views.node_action, name="node_action"),
]
