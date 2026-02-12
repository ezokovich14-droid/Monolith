#!/bin/bash
set -e

# Attendre que la base de données soit prête (si PostgreSQL)
# echo "Attente de la base de données..."
# while ! nc -z db 5432; do
#   sleep 0.1
# done
# echo "Base de données prête!"

# Appliquer les migrations
echo "Application des migrations Django..."
python manage.py migrate --noinput

# Créer un superuser si aucun n'existe
echo "Vérification du superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser créé: admin/admin123')
else:
    print('Superuser déjà existant')
"

# Collecter les fichiers statiques
echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear

# Démarrer l'application
echo "Démarrage de l'application Django..."
exec "$@"
