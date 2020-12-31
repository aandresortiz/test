from django.urls import path

from . import views

urlpatterns = [
    # api
    path("orders/", views.OrderListView.as_view()),
    path("orders/<int:pk>", views.OrderView.as_view()),
]
