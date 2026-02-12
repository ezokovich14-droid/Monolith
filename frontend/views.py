from django.shortcuts import render
import time
import os

# 🚨 DÉMONSTRATION CRASH AU DÉMARRAGE (décommente pour crash)
# raise Exception("💥 CRASH AU DÉMARRAGE DU MONOLITHE !")

def home(request):
    # 🚨 DÉMONSTRATION CRASH : Décommente pour crash TOUTE l'app
    # time.sleep(30)  # Timeout de 30 secondes
    
    return render(request, 'home.html')


def products(request):
    # 🚨 DÉMONSTRATION CRASH : Décommente pour crash TOUTE l'app
    # raise Exception("CRASH DU MONOLITHE - Plus rien ne fonctionne !")
    
    return render(request, 'products.html')


def orders(request):
    # 🚨 DÉMONSTRATION CRASH : Décommente pour crash TOUTE l'app
    # import os
    # os._exit(1)  # Kill immédiat du processus
    
    return render(request, 'orders.html')


def dashboard(request):
    # 🚨 DÉMONSTRATION CRASH : Décommente pour crash TOUTE l'app
    # while True:  # Boucle infinie = CPU 100%
    #     pass
    
    return render(request, 'dashboard.html')


def test_api(request):
    return render(request, 'test_api.html')


# 🛡️ DÉMONSTRATION TOLÉRANCE : Fonction qui ne crash pas tout
def resilient_feature(request):
    try:
        # Simulation d'une erreur qui ne crash que cette fonction
        result = 1 / 0  # Division par zéro
        return render(request, 'home.html', {'result': result})
    except Exception as e:
        # 🎯 Le monolithe continue de fonctionner malgré l'erreur
        print(f"Erreur isolée : {e}")
        return render(request, 'home.html', {
            'error': 'Fonctionnalité temporairement indisponible',
            'rest_of_app': 'L application continue de fonctionner !'
        })


# 🚨 DÉMONSTRATION CRASH TOTAL : Endpoint qui crash tout le monolithe
def crash_everything(request):
    """Démonstration : Un bug dans une partie crash TOUTE l'application"""
    
    # Option 1: Exception non gérée = crash total
    # raise Exception("💥 CRASH TOTAL DU MONOLITHE !")
    
    # Option 2: Boucle infinie = CPU 100%
    # while True:
    #     pass
    
    # Option 3: Memory leak = crash progressif
    # big_data = []
    # while True:
    #     big_data.append("x" * 1000000)  # Consomme toute la RAM
    
    return render(request, 'home.html', {'message': 'Monolithe stable'})
