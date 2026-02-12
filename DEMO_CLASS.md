# 🎭 DÉMONSTRATION POUR LA CLASSE : Avantages/Inconvénients du Monolithique

## 🚨 **DÉMO 1 : CRASH TOTAL DU MONOLITHE**

### 📍 **Où modifier :**
Fichier : `frontend/views.py`

### 🔧 **Comment crasher TOUTE l'application :**

#### **Option A : Exception non gérée**
```python
def products(request):
    raise Exception("💥 CRASH TOTAL DU MONOLITHE !")
    return render(request, 'products.html')
```
**Résultat :** TOUTE l'application devient inaccessible (home, orders, dashboard, API)

#### **Option B : Timeout**
```python
def orders(request):
    time.sleep(60)  # Timeout de 60 secondes
    return render(request, 'orders.html')
```
**Résultat :** Timeout sur toutes les pages

#### **Option C : CPU 100%**
```python
def dashboard(request):
    while True:  # Boucle infinie
        pass
    return render(request, 'dashboard.html')
```
**Résultat :** CPU à 100%, plus rien ne répond

#### **Option D : Memory leak**
```python
def home(request):
    big_data = []
    while True:
        big_data.append("x" * 1000000)  # Consomme toute la RAM
    return render(request, 'home.html')
```
**Résultat :** RAM saturée, crash du serveur

### 🎯 **URLs de test :**
- http://127.0.0.1:8000/demo/crash-total/ (crash total)
- http://127.0.0.1:8000/products/ (décommente une ligne pour crash)
- http://127.0.0.1:8000/orders/ (décommente une ligne pour crash)
- http://127.0.0.1:8000/dashboard/ (décommente une ligne pour crash)

---

## 🛡️ **DÉMO 2 : TOLÉRANCE AUX PANNES**

### 📍 **Où modifier :**
Fichier : `frontend/views.py` → fonction `resilient_feature()`

### 🔧 **Comment montrer la tolérance :**

```python
def resilient_feature(request):
    try:
        result = 1 / 0  # Erreur isolée
        return render(request, 'home.html', {'result': result})
    except Exception as e:
        # 🎯 Le monolithe continue de fonctionner !
        return render(request, 'home.html', {
            'error': 'Fonctionnalité indisponible',
            'rest_of_app': 'Le reste de l\'app fonctionne !'
        })
```

### 🎯 **URL de test :**
- http://127.0.0.1:8000/demo/resilient/

---

## 🎓 **SCÉNARIO PÉDAGOGIQUE**

### **Étape 1 : Montrer la stabilité**
1. Lancer le serveur : `python manage.py runserver`
2. Montrer que tout fonctionne :
   - http://127.0.0.1:8000/ ✅
   - http://127.0.0.1:8000/products/ ✅
   - http://127.0.0.1:8000/orders/ ✅
   - http://127.0.0.1:8000/api/products/ ✅

### **Étape 2 : Démontrer le crash**
1. Décommenter une ligne dans `views.py`
2. Rafraîchir toutes les pages
3. **Résultat :** Tout est cassé ! 💥

### **Étape 3 : Montrer la tolérance**
1. Visiter http://127.0.0.1:8000/demo/resilient/
2. **Résultat :** Message d'erreur mais le reste continue ✅

---

## 💡 **POINTS CLÉS À EXPLIQUER**

### **🚨 Inconvénients du Monolithique :**
- **Point de défaillance unique** : Un bug = tout l'app down
- **Déploiement global** : Impossible de déployer qu'une partie
- **Scaling complexe** : Tout doit scaler ensemble
- **Impact partagé** : Une fonction lente ralentit tout

### **🛡️ Avantages du Monolithique :**
- **Gestion d'erreurs locale** : try/catch efficace
- **Transactions atomiques** : Cohérence garantie
- **Performance** : Pas de latence réseau
- **Développement simple** : Tout au même endroit

---

## 🎭 **DÉMONSTRATION LIVE**

### **Script de présentation :**

"Regardez, actuellement tout fonctionne parfaitement :
- Home ✅
- Products ✅  
- Orders ✅
- Dashboard ✅

Maintenant, je vais introduire un SEUL bug dans la fonction products..."

*(Décommente la ligne dans products())*

"Et maintenant... plus rien ne fonctionne ! 💥
- Home ❌
- Products ❌
- Orders ❌  
- Dashboard ❌
- API ❌

**C'est le principal inconvénient du monolithique : un point de défaillance unique !**

Mais regardons comment on peut gérer les erreurs proprement..."

*(Visite /demo/resilient/)*

"Vous voyez ? J'ai une erreur, mais le reste de l'application continue de fonctionner. C'est la tolérance aux pannes avec une bonne gestion d'erreurs."

---

## 🔧 **COMMENT RÉPARER**

Pour réparer après la démo :
1. Commenter/décommenter les lignes dans `views.py`
2. Redémarrer le serveur : `python manage.py runserver`
3. Tout revient à la normale ✅

---

## 🎯 **CONCLUSION**

**Le monolithique est comme une maison :**
- ✅ **Facile à construire** et à gérer
- ✅ **Tout est connecté** rapidement
- ❌ **Un problème dans les fondations = toute la maison s'effondre**
- ❌ **Impossible de rénover qu'une seule pièce**

**Les microservices sont comme un village :**
- ✅ **Une maison en feu = le village continue**
- ✅ **Chaque maison peut être rénovée séparément**
- ❌ **Complexité des communications entre les maisons**
- ❌ **Plus cher et plus long à construire**

---

**🚀 Prêt pour votre démo en classe ?**
