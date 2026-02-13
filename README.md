# 🛍️ E-Commerce Monolithique - Django

> **Architecture monolithique** pour démonstration des avantages et limites en classe

## 🚀 Quick Start

```bash
git clone https://github.com/ezokovich14-droid/Monoith.git
cd monolith
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🌐 Accès

- **Application** : http://127.0.0.1:8000/
- **Admin Django** : http://127.0.0.1:8000/admin/
- **API REST** : http://127.0.0.1:8000/api/
- **Démo crash** : http://127.0.0.1:8000/demo/crash-total/
- **Démo tolérance** : http://127.0.0.1:8000/demo/resilient/

## 📦 Installation Complète

### 1. Environnement virtuel
```bash
cd monolith
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 2. Dépendances
```bash
pip install -r requirements.txt
```

### 3. Base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Superuser
```bash
python manage.py createsuperuser
```

### 5. Données de démo
```bash
python create_demo_data.py
```

### 6. Lancement
```bash
python manage.py runserver
```

## 🎭 Scénarios de Test pour Démonstration

### 🚨 Scénario 1 : CRASH TOTAL DU MONOLITHE

**Objectif :** Démontrer qu'un bug dans une partie crash TOUTE l'application

**Étapes :**
1. **Lancer l'application** : `python manage.py runserver --noreload`
2. **Vérifier que tout fonctionne** :
   - http://127.0.0.1:8000/ ✅
   - http://127.0.0.1:8000/products/ ✅
   - http://127.0.0.1:8000/orders/ ✅
   - http://127.0.0.1:8000/dashboard/ ✅
   - http://127.0.0.1:8000/api/products/ ✅

3. **Décommenter une ligne de crash** dans `frontend/views.py` :
   ```python
   def products(request):
       raise Exception("💥 CRASH DU MONOLITHE - Plus rien ne fonctionne !")
       return render(request, 'products.html')
   ```

4. **Redémarrer le serveur** : `python manage.py runserver --noreload`

5. **Résultat :** TOUTES les pages retournent des erreurs 500 ❌
   - http://127.0.0.1:8000/ ❌
   - http://127.0.0.1:8000/admin/ ❌
   - http://127.0.0.1:8000/api/ ❌

**Conclusion :** "Un seul point de défaillance = toute l'application down !"

### 🛡️ Scénario 2 : TOLÉRANCE AUX PANNES

**Objectif :** Démontrer la gestion d'erreurs élégante

**Étapes :**
1. **Visiter** : http://127.0.0.1:8000/demo/resilient/
2. **Observer** : Message d'erreur mais le reste de l'app continue ✅
3. **Tester d'autres pages** : Elles fonctionnent toujours ✅

**Conclusion :** "Avec une bonne gestion d'erreurs, le monolithe peut être résilient !"

### 🌐 Scénario 3 : DÉPLOIEMENT EN PRODUCTION

**Objectif :** Démontrer le déploiement facile avec Railway

**Étapes :**
1. **Installer Railway CLI** : `npm install -g @railway/cli`
2. **Se connecter** : `railway login`
3. **Lier le projet** : `railway link`
4. **Déployer** : `railway up`
5. **URL de production** : https://striking-reprieve.railway.app

**Conclusion :** "Le monolithe en production = simplicité et rapidité !"

## 🧪 Tests API

### Créer un produit
```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop Dell",
    "description": "Laptop puissant",
    "price": "850.00",
    "stock": 10
  }'
```

### Créer une commande
```bash
curl -X POST http://127.0.0.1:8000/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "product_id": 1,
    "quantity": 2
  }'
```

## 📊 Architecture

### 🗄️ Base de données unique (SQLite/PostgreSQL)
- `users_customuser` : Utilisateurs
- `products_product` : Produits  
- `orders_order` : Commandes
- `orders_orderitem` : Détails des commandes

### 🌐 URLs principales
```
/                    → Home
/products/           → Produits
/orders/             → Commandes
/dashboard/          → Dashboard
/admin/              → Admin Django
/api/products/        → API Produits
/api/orders/          → API Commandes
/api/users/           → API Utilisateurs
/demo/crash-total/    → Démo crash
/demo/resilient/      → Démo tolérance
```

## ✅ Avantages du Monolithique

1. **🚀 Déploiement simple** : Une seule application à déployer
2. **⚡ Performance** : Pas de latence réseau entre services
3. **🔧 Debugging facile** : Tout dans un seul processus
4. **💾 Transactions atomiques** : Cohérence garantie
5. **📦 Simplicité** : Moins de complexité opérationnelle

## ❌ Limites du Monolithique

1. **💥 Point de défaillance unique** : Un bug = tout l'app down
2. **📈 Scaling complexe** : Tout doit scaler ensemble
3. **🔄 Déploiements globaux** : Impossible de déployer qu'une partie
4. **🎯 Technologie unique** : Difficile de mixer les techno

## 🐳 Docker

### Déploiement avec Docker
```bash
docker-compose up -d
```

### URLs Docker
- **Application** : http://localhost/
- **Admin** : http://localhost/admin/
- **API** : http://localhost/api/

## 🌐 Production

### Railway (Recommandé)
1. **Installer** : `npm install -g @railway/cli`
2. **Connecter** : `railway login`
3. **Déployer** : `railway up`
4. **URL** : https://striking-reprieve.railway.app

### Variables d'environnement
```
DEBUG=False
ALLOWED_HOSTS=*.railway.app
SECRET_KEY=votre-clé-secrète
```

## 🎯 Pour la Présentation

### Script de démo
1. **Montrer la stabilité** : Toutes les pages fonctionnent
2. **Crash contrôlé** : Décommenter une ligne = tout down
3. **Gestion d'erreurs** : `/demo/resilient/` continue de fonctionner
4. **Production** : URL Railway accessible mondialement

### Messages clés
- "Le monolithe = simplicité mais fragilité"
- "Un point de défaillance = impact global"
- "La gestion d'erreurs est cruciale"
- "Le déploiement reste très simple"

## 📚 Ressources

- **Documentation Django** : https://docs.djangoproject.com/
- **Django REST Framework** : https://www.django-rest-framework.org/
- **Railway** : https://railway.app/
- **Docker** : https://docs.docker.com/

---

**🎓 Projet éducatif pour démontrer l'architecture monolithique vs microservices**
