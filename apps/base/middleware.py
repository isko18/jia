from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class RedirectToHomeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path

        # Проверяем, если это первичный заход на сайт с префиксом
        if path.startswith('/ru/') or path.startswith('/en/') or path.startswith('/ky/'):
            # Перенаправляем на главную страницу
            return redirect('/')
        
        # Продолжаем обработку запроса
        return None
