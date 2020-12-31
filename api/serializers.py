from rest_framework import serializers

from api.models import Order, OrderItem, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class OrderListSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ["date", "status", "user", "total_items", "total"]


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["description", "quantity", "price"]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ["date", "status", "user", "total_items", "total", "items"]
