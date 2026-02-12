"""
Serializers pour l'API orders
"""
from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer pour les articles de commande
    """
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price', 'subtotal']
        read_only_fields = ['id', 'unit_price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer pour les commandes
    """
    items = OrderItemSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    product_name = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'user_name', 'status', 
            'total_amount', 'items', 'created_at', 'updated_at',
            'product_name', 'quantity'
        ]
        read_only_fields = ['id', 'total_amount', 'created_at', 'updated_at']

    def get_product_name(self, obj):
        """Retourner le nom du premier produit"""
        first_item = obj.items.first()
        return first_item.product.name if first_item else None

    def get_quantity(self, obj):
        """Retourner la quantité totale d'items"""
        return sum(item.quantity for item in obj.items.all())


class OrderCreateSerializer(serializers.Serializer):
    """
    Serializer pour créer une commande simple
    """
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate_product_id(self, value):
        """
        Valider que le produit existe
        """
        from products.models import Product
        try:
            Product.objects.get(id=value)
            return value
        except Product.DoesNotExist:
            raise serializers.ValidationError("Ce produit n'existe pas")

    def validate_user_id(self, value):
        """
        Valider que l'utilisateur existe
        """
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            User.objects.get(id=value)
            return value
        except User.DoesNotExist:
            raise serializers.ValidationError("Cet utilisateur n'existe pas")
