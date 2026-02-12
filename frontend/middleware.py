"""
Middleware pour démonstration de crash
"""
import time

class CrashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 🚨 Crash qui ne peut pas être évité par le reloader
        if request.path == '/products/' and request.GET.get('crash') == 'true':
            time.sleep(30)  # Timeout de 30 secondes
            # OU :
            # raise Exception("💥 CRASH MIDDLEWARE !")
        
        response = self.get_response(request)
        return response
