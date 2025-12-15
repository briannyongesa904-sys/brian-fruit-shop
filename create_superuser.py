# create_superuser.py
import os
import django
from django.contrib.auth.models import User

# Set Django settings module (replace 'your_project.settings' with your actual settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

USERNAME = 'ReenB'
EMAIL = 'briannyongesa904@gmail.com'  # optional
PASSWORD = 'Nyongesa@254'

# Create superuser if it doesn't exist
if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
