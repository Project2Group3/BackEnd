import os
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publish.settings')
django.setup()

# Import the User model
from models import User
from serializers import UserSerializer
# Create a test user
def create_test_user():
    if not User.objects.filter(username='tester1').exists():
        request={
            "name": "BOB",
            "email": "bob@example.com",
            "username": "tester1"
            }
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # user= UserSerializer(({
        #     "name": "BOB",
        #     "email": "bob@example.com",
        #     "username": "tester1"
        #     }
        # ).data)
        # user = User.objects.create_user(username='testuser', password='testpassword')
        # user.name = 'Tester1'
        # user.email = 'testuser@example.com'
        # user.username= 'testuser'

        # user.save()
        print("Test user created:", serializer)
    else:
        print("User already exists.")

if __name__ == '__main__':
    create_test_user()