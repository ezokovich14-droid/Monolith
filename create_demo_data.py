#!/usr/bin/env python
"""
Script pour créer des données de démonstration
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from products.models import Product
from users.models import CustomUser
from orders.models import Order, OrderItem

def create_demo_data():
    print("Création des données de démonstration...")
    
    # Créer des utilisateurs
    users = []
    for i in range(5):
        user, created = CustomUser.objects.get_or_create(
            email=f'user{i+1}@example.com',
            defaults={
                'username': f'user{i+1}',
                'first_name': f'User{i+1}',
                'last_name': f'Test{i+1}',
                'is_active': True
            }
        )
        if created:
            user.set_password('password123')
            user.save()
        users.append(user)
    
    # Créer des produits
    products = []
    product_data = [
        {
            'name': 'Laptop Dell XPS 15',
            'description': 'Ordinateur portable haute performance avec écran 4K',
            'price': 1299.99,
            'stock': 15
        },
        {
            'name': 'iPhone 15 Pro',
            'description': 'Dernier modèle d\'iPhone avec processeur A17 Pro',
            'price': 1199.00,
            'stock': 25
        },
        {
            'name': 'MacBook Air M2',
            'description': 'Ultra-léger et ultra-performant',
            'price': 1499.99,
            'stock': 8
        },
        {
            'name': 'Samsung Galaxy S24',
            'description': 'Smartphone Android haut de gamme',
            'price': 899.99,
            'stock': 30
        },
        {
            'name': 'iPad Pro 12.9"',
            'description': 'Tablette professionnelle avec écran Liquid Retina XDR',
            'price': 1099.00,
            'stock': 12
        },
        {
            'name': 'AirPods Pro 2',
            'description': 'Écouteurs sans fil avec réduction de bruit active',
            'price': 249.99,
            'stock': 50
        },
        {
            'name': 'Apple Watch Series 9',
            'description': 'Montre connectée avec capteurs de santé avancés',
            'price': 399.99,
            'stock': 20
        },
        {
            'name': 'Sony WH-1000XM5',
            'description': 'Casque audio à réduction de bruit',
            'price': 349.99,
            'stock': 18
        }
    ]
    
    for data in product_data:
        product, created = Product.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        products.append(product)
    
    # Créer des commandes
    import random
    from datetime import datetime, timedelta
    
    statuses = ['pending', 'processing', 'shipped', 'delivered', 'cancelled']
    
    for i in range(15):
        user = random.choice(users)
        product = random.choice(products)
        quantity = random.randint(1, 3)
        
        # Vérifier si le produit a assez de stock
        if product.stock >= quantity:
            # Créer la commande
            order = Order.objects.create(
                user=user,
                status=random.choice(statuses),
                created_at=datetime.now() - timedelta(days=random.randint(0, 30))
            )
            
            # Créer l'item de commande
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )
            
            # Réduire le stock
            product.reduce_stock(quantity)
    
    print("Données de démonstration créées avec succès !")
    print(f"- {CustomUser.objects.count()} utilisateurs créés")
    print(f"- {Product.objects.count()} produits créés")
    print(f"- {Order.objects.count()} commandes créées")

if __name__ == '__main__':
    create_demo_data()
