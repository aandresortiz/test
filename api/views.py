from django.db.models import Count, Sum
from rest_framework import filters, generics

from api.models import Order
from api.serializers import OrderListSerializer, OrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = self.queryset.annotate(
            total_items=Count("items"), total=Sum("items__price")
        )

        status = self.request.query_params.get("status", None)
        date = self.request.query_params.get("date", None)
        total = self.request.query_params.get("total", None)

        if status is not None:
            queryset = queryset.filter(status=status)

        if date is not None:
            queryset = queryset.filter(date=date)

        if total is not None:
            queryset = queryset.filter(total=total)

        return queryset

    serializer_class = OrderListSerializer


class OrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = self.queryset.annotate(
            total_items=Count("items"), total=Sum("items__price")
        )
        return queryset

    serializer_class = OrderSerializer
