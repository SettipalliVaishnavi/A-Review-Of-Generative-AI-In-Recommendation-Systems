
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Recommendation_Systems.settings')
django.setup()

from users.models import UserRegistrationModel

loginid = 'chatura'
password = 'Madhu@1729'

user, created = UserRegistrationModel.objects.get_or_create(
    loginid=loginid,
    defaults={
        'name': 'Chatura',
        'password': password,
        'mobile': '1234567890',
        'email': 'chatura@example.com',
        'locality': 'Local',
        'address': 'Test Address',
        'city': 'Test City',
        'state': 'Test State',
        'status': 'activated'
    }
)

if not created:
    user.password = password
    user.status = 'activated'
    user.save()
    print(f"User {loginid} updated and activated.")
else:
    print(f"User {loginid} created and activated.")
