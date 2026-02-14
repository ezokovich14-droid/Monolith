# 🏗️ SCHÉMA ARCHITECTURAL - MONOLITHE E-COMMERCE

## 📋 VUE D'ENSEMBLE

```mermaid
graph TB
    subgraph "🌐 MONOLITHE DJANGO"
        subgraph "🎨 Frontend Layer"
            A[Home Page]
            B[Products Page]
            C[Orders Page]
            D[Dashboard Admin]
            E[API Endpoints]
        end
        
        subgraph "🧠 Business Logic Layer"
            F[User Management]
            G[Product Management]
            H[Order Management]
            I[Notification Service]
        end
        
        subgraph "🗄️ Data Layer"
            J[(SQLite/PostgreSQL)]
            K[Django ORM]
        end
        
        subgraph "🔧 Configuration"
            L[Settings]
            M[URLs Routing]
            N[Middleware]
        end
    end
    
    subgraph "🌍 External Services"
        O[Railway Hosting]
        P[Docker Container]
        Q[Nginx Reverse Proxy]
    end
    
    A --> F
    B --> G
    C --> H
    D --> F
    D --> G
    D --> H
    E --> F
    E --> G
    E --> H
    
    F --> K
    G --> K
    H --> K
    I --> K
    
    K --> J
    
    L --> M
    M --> N
    N --> A
    N --> B
    N --> C
    N --> D
    N --> E
    
    O --> P
    P --> Q
```

## 🎯 FONCTIONNEMENT INTERNE

### 📊 Flux de Données

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant F as Frontend
    participant V as Views
    participant M as Models
    participant D as Database
    
    U->>F: 1. Visite page
    F->>V: 2. Request HTTP
    V->>M: 3. Query ORM
    M->>D: 4. SQL Query
    D-->>M: 5. Data
    M-->>V: 6. Objects
    V-->>F: 7. Template + Context
    F-->>U: 8. HTML Response
```

## 🏛️ STRUCTURE DES MODULES

### 📦 Détail par Module

```mermaid
graph LR
    subgraph "👥 Users Module"
        U1[CustomUser Model]
        U2[User Views]
        U3[User Serializers]
        U4[User URLs]
    end
    
    subgraph "📦 Products Module"
        P1[Product Model]
        P2[Product Views]
        P3[Product Serializers]
        P4[Product URLs]
    end
    
    subgraph "🛒 Orders Module"
        O1[Order Model]
        O2[Order Views]
        O3[Order Serializers]
        O4[Order URLs]
    end
    
    subgraph "🔔 Notifications Module"
        N1[Notification Model]
        N2[Notification Views]
        N3[Notification Serializers]
    end
    
    subgraph "🎨 Frontend Module"
        F1[Home Template]
        F2[Products Template]
        F3[Orders Template]
        F4[Dashboard Template]
    end
```

## 🔄 INTERCONNEXION DES SERVICES

### 🌐 Points d'Entrée Uniques

```mermaid
graph TD
    subgraph "🚀 Single Entry Point"
        A[Django Runserver<br/>Port 8000]
    end
    
    subgraph "📡 URL Dispatcher"
        B[/ → Home]
        C[/products/ → Products]
        D[/orders/ → Orders]
        E[/admin/ → Admin]
        F[/api/ → REST API]
    end
    
    subgraph "🎭 Demo Endpoints"
        G[/demo/crash-total/ → Crash]
        H[/demo/resilient/ → Tolérance]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    A --> G
    A --> H
```

## 🗄️ ARCHITECTURE DE DONNÉES

### 📊 Tables Unifiées

```mermaid
erDiagram
    CUSTOM_USER {
        int id PK
        string username
        string email
        string first_name
        string last_name
        boolean is_staff
        datetime date_joined
    }
    
    PRODUCT {
        int id PK
        string name
        text description
        decimal price
        int stock
        boolean is_active
        datetime created_at
        datetime updated_at
    }
    
    ORDER {
        int id PK
        int user_id FK
        datetime order_date
        string status
        decimal total_amount
    }
    
    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }
    
    NOTIFICATION {
        int id PK
        int user_id FK
        string message
        boolean is_read
        datetime created_at
    }
    
    CUSTOM_USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : appears_in
    CUSTOM_USER ||--o{ NOTIFICATION : receives
```

## 🔄 CYCLE DE VIE D'UNE REQUÊTE

### 📡 Processus Complet

```mermaid
flowchart TD
    A[🌐 Client Request] --> B{🔍 URL Analysis}
    B -->|/| C[🏠 Home View]
    B -->|/products/| D[📦 Products View]
    B -->|/orders/| E[🛒 Orders View]
    B -->|/admin/| F[🔧 Admin View]
    B -->|/api/| G[🔌 API View]
    B -->|/demo/| H[🎭 Demo View]
    
    C --> I[🧠 Business Logic]
    D --> I
    E --> I
    F --> I
    G --> I
    H --> I
    
    I --> J[🗄️ Database Query]
    J --> K[💾 SQLite/PostgreSQL]
    K --> L[📤 Response Data]
    L --> M[🎨 Template Rendering]
    M --> N[🌐 HTML Response]
```

## 🚨 GESTION DES ERREURS

### 🛡️ Points de Défaillance

```mermaid
graph TD
    A[🌐 User Request] --> B{🔍 Error Check}
    B -->|No Error| C[✅ Normal Flow]
    B -->|Exception| D[🚨 Error Handler]
    B -->|Crash Demo| E[💥 Crash Middleware]
    
    C --> F[📤 Success Response]
    D --> G[🛡️ Try/Catch Block]
    E --> H[💀 Total Crash]
    
    G --> I[📝 Error Log]
    G --> J[🔄 Graceful Degradation]
    H --> K[❌ Service Unavailable]
    
    I --> L[🌐 Error Page]
    J --> M[⚠️ Limited Functionality]
    F --> N[✅ Full Functionality]
```

## 🌍 DÉPLOIEMENT PRODUCTION

### 🐳 Architecture Docker

```mermaid
graph TB
    subgraph "🌐 Railway Cloud"
        subgraph "🐳 Docker Container"
            A[Django App<br/>Port 8000]
            B[Gunicorn<br/>WSGI Server]
            C[Nginx<br/>Reverse Proxy]
        end
        
        subgraph "🗄️ Database"
            D[PostgreSQL<br/>Managed Service]
        end
        
        subgraph "🔧 Infrastructure"
            E[Load Balancer]
            F[SSL Certificate]
            G[Health Checks]
        end
    end
    
    H[🌐 Internet] --> E
    E --> C
    C --> A
    A --> B
    B --> D
    G --> A
```

## 📊 MONITORING ET OBSERVABILITÉ

### 🔍 Points de Surveillance

```mermaid
graph LR
    subgraph "📊 Monitoring Stack"
        A[Application Logs]
        B[Health Checks]
        C[Performance Metrics]
        D[Error Tracking]
    end
    
    subgraph "🚨 Alerting"
        E[Service Down]
        F[High Error Rate]
        G[Slow Response]
    end
    
    subgraph "🔧 Actions"
        H[Auto Restart]
        I[Scale Up]
        J[Notify Admin]
    end
    
    A --> E
    B --> E
    C --> F
    D --> F
    
    E --> H
    F --> I
    G --> J
```

## 🎯 AVANTAGES ARCHITECTURAUX

### ✅ Forces du Monolithique

1. **🚀 Déploiement Unifié**
   - Un seul conteneur Docker
   - Une seule base de code
   - Un seul processus à monitorer

2. **⚡ Performance Optimale**
   - Pas de latence réseau
   - Transactions atomiques
   - Partage de mémoire efficace

3. **🔧 Debugging Simplifié**
   - Stack trace complète
   - Un seul processus à analyser
   - Logs centralisés

4. **💾 Cohérence des Données**
   - Une seule base de données
   - Transactions ACID garanties
   - Pas de sync complexes

### ❌ Faiblesses du Monolithique

1. **💥 Point de Défaillance Unique**
   - Un bug = toute l'application down
   - Difficile d'isoler les problèmes
   - Impact maximal des erreurs

2. **📈 Scaling Complexe**
   - Tout doit scaler ensemble
   - Pas de scaling granulaire
   - Coûts optimisation difficiles

3. **🔄 Déploiements Globaux**
   - Impossible de déployer qu'une partie
   - Temps de déploiement longs
   - Risques élevés par changement

---

## 🎓 CONCLUSION PÉDAGOGIQUE

### 🎯 Messages Clés pour la Présentation

1. **"Le monolithe = simplicité architecturale"**
   - Tout est dans un seul projet
   - Facile à comprendre et développer
   - Déploiement simple

2. **"Mais cette simplicité a un prix : la fragilité"**
   - Un point de défaillance unique
   - Impact global des erreurs
   - Difficile à faire évoluer

3. **"La solution : monitoring et gestion d'erreurs"**
   - Détection rapide des problèmes
   - Isolation des erreurs critiques
   - Dégradation gracieuse

4. **"L'alternative : les microservices"**
   - Indépendance des services
   - Isolation des pannes
   - Complexité opérationnelle

---

**🏗️ Ce schéma montre comment tous les services sont liés dans notre monolithe !**
