import os
import sys
import django
from django.contrib.auth import get_user_model

# Добавляем путь к модулю bif в PYTHONPATH
sys.path.append('/BIF')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bif.settings.base')
django.setup()

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser {username} created.')
else:
    print(f'Superuser {username} already exists.')
