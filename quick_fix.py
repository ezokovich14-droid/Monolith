#!/usr/bin/env python
"""
Script rapide pour créer les données manquantes
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from products.models import Product
from orders.models import Order, OrderItem
from django.db import transaction

User = get_user_model()

def create_missing_data():
    print("🔧 Création des données manquantes...")
    
    # 1. Créer un superuser si aucun utilisateur
    if User.objects.count() == 0:
        print("📝 Création d'un superuser...")
        user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print(f"✅ Superuser créé: {user.username}")
    else:
        print(f"✅ Utilisateurs existants: {User.objects.count()}")
    
    # 2. Créer des utilisateurs normaux
    for i in range(1, 4):
        username = f'user{i}'
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=f'{username}@example.com',
                password='password123',
                first_name=f'User{i}',
                last_name='Test'
            )
            print(f"✅ Utilisateur créé: {user.username}")
    
    # 3. Créer quelques commandes si produits existent
    products = list(Product.objects.all()[:3])
    users = list(User.objects.all()[:3])
    
    if products and users:
        print("📦 Création de commandes...")
        
        with transaction.atomic():
            for i in range(3):
                user = users[i]
                product = products[i]
                quantity = 1
                
                if product.stock >= quantity:
                    # Créer la commande
                    order = Order.objects.create(
                        user=user,
                        status=['pending', 'processing', 'delivered'][i],
                        total_amount=product.price * quantity
                    )
                    
                    # Créer l'item
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        unit_price=product.price,
                        subtotal=product.price * quantity
                    )
                    
                    # Réduire le stock
                    product.stock -= quantity
                    product.save()
                    
                    print(f"✅ Commande #{order.id}: {product.name} pour {user.username}")
    
    print("\n🎉 Données créées avec succès !")
    print(f"📊 Résumé:")
    print(f"   - Utilisateurs: {User.objects.count()}")
    print(f"   - Produits: {Product.objects.count()}")
    print(f"   - Commandes: {Order.objects.count()}")
    print(f"\n🔑 Connexions:")
    print(f"   - Admin: admin / admin123")
    print(f"   - User1: user1 / password123")
    print(f"   - User2: user2 / password123")
    print(f"   - User3: user3 / password123")

if __name__ == '__main__':
    create_missing_data()
