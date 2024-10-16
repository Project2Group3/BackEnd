import os
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publish.settings')
django.setup()

# Import the User model
from django.contrib.auth.models import User

# Create a test user
def create_test_user():
    if not User.objects.filter(username='testuser').exists():
        user = User.objects.create_user(username='testuser', password='testpassword')
        user.first_name = 'Test'
        user.last_name = 'User'
        user.email = 'testuser@example.com'
        user.save()
        print("Test user created:", user)
    else:
        print("User already exists.")

if __name__ == '__main__':
    create_test_user()