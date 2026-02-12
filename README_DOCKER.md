# 🐳 Dockerisation - E-Commerce Monolithique

## 🚀 Déploiement rapide avec Docker

### Prérequis
- Docker et Docker Compose installés
- Git (pour cloner le projet)

### 1. Cloner le projet
```bash
git clone <votre-repo>
cd projet-monolith-microservices-complet/monolith
```

### 2. Construire et lancer
```bash
# Construire l'image Docker
docker build -t ecommerce-monolith .

# Ou avec Docker Compose (recommandé)
docker-compose up -d
```

### 3. Accéder à l'application
- **Application** : http://localhost
- **API** : http://localhost/api/
- **Admin Django** : http://localhost/admin/

## 📁 Fichiers Docker créés

### `Dockerfile`
- Image Python 3.11 slim optimisée
- Installation des dépendances
- Configuration de l'environnement
- Exposition du port 8000

### `docker-compose.yml`
- Service web (Django)
- Service nginx (reverse proxy)
- Volumes pour la persistance des données
- Health checks
- Configuration de production

### `nginx.conf`
- Reverse proxy vers Django
- Service des fichiers statiques
- Optimisation des performances
- Health check endpoint

### `.dockerignore`
- Exclusion des fichiers inutiles
- Réduction de la taille de l'image

## 🛠️ Commandes utiles

### Démarrer/Arrêter
```bash
# Démarrer tous les services
docker-compose up -d

# Arrêter tous les services
docker-compose down

# Voir les logs
docker-compose logs -f web

# Reconstruire après modification
docker-compose up -d --build
```

### Maintenance
```bash
# Entrer dans le conteneur Django
docker-compose exec web bash

# Créer un superuser
docker-compose exec web python manage.py createsuperuser

# Appliquer les migrations
docker-compose exec web python manage.py migrate

# Vider les logs
docker-compose logs -f > /dev/null
```

## 🌐 Déploiement en production

### Option 1: Docker Hub
```bash
# Construire et pousser
docker build -t votre-username/ecommerce-monolith .
docker push votre-username/ecommerce-monolith

# Pull et run sur le serveur
docker run -d -p 80:8000 votre-username/ecommerce-monolith
```

### Option 2: Cloud providers
- **AWS ECS** : `docker-compose up` avec configuration ECS
- **Google Cloud Run** : `gcloud run deploy`
- **Azure Container Instances** : Portail Azure ou CLI
- **Heroku** : `heroku container:push web`

### Option 3: VPS classique
```bash
# Sur le serveur
git clone <votre-repo>
cd projet-monolith-microservices-complet/monolith
docker-compose up -d

# Configurer un domaine (optionnel)
# Modifier nginx.conf pour votre domaine
# Ajouter un certificat SSL avec Let's Encrypt
```

## 🔧 Configuration production

### Variables d'environnement
```bash
# Dans docker-compose.yml
environment:
  - DEBUG=False
  - SECRET_KEY=votre-cle-secrete
  - ALLOWED_HOSTS=votredomaine.com,www.votredomaine.com
  - DATABASE_URL=postgresql://user:pass@host:port/dbname  # Si vous changez de BDD
```

### Base de données PostgreSQL (optionnel)
```yaml
# Ajouter dans docker-compose.yml
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ecommerce
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
```

## 📊 Monitoring

### Health checks
```bash
# Vérifier l'état des services
docker-compose ps

# Health check endpoint
curl http://localhost/health
```

### Logs
```bash
# Logs en temps réel
docker-compose logs -f

# Logs spécifiques
docker-compose logs web
docker-compose logs nginx
```

## 🔒 Sécurité

### SSL/TLS
```bash
# Avec Let's Encrypt (recommandé)
certbot --nginx -d votredomaine.com

# Ou certificat auto-signé pour développement
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/private.key -out ssl/certificate.crt
```

### Bonnes pratiques
- Changer les clés secrètes par défaut
- Utiliser HTTPS en production
- Limiter l'accès à `/admin/`
- Mettre à jour régulièrement les dépendances

## 🚀 Avantages de cette solution Docker

✅ **Déploiement instantané** : Une seule commande
✅ **Environnement isolé** : Pas de conflits de dépendances
✅ **Scalabilité** : Facile à scaler avec plusieurs conteneurs
✅ **Portabilité** : Fonctionne partout où Docker tourne
✅ **Persistance** : Données sauvegardées avec volumes
✅ **Monitoring** : Health checks intégrés
✅ **Performance** : Nginx + Django optimisé

## 🎯 Prochaines étapes

1. **CI/CD** : GitHub Actions pour déploiement automatique
2. **Monitoring avancé** : Prometheus + Grafana
3. **Backup automatique** : Scripts de sauvegarde BDD
4. **Load balancing** : Plusieurs instances Django
5. **CDN** : CloudFlare pour les fichiers statiques

---

**🐳 Avec Docker, votre e-commerce monolithique est prêt pour la production en quelques minutes !**
