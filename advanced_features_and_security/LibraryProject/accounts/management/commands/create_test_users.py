from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_data = [
            {"username": "admin_user", "password": "admin123", "group": "Admins"},
            {"username": "editor_user", "password": "editor123", "group": "Editors"},
            {"username": "viewer_user", "password": "viewer123", "group": "Viewers"},
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(username=user_data["username"])
            if created:
                user.set_password(user_data["password"])
                user.save()
                group = Group.objects.get(name=user_data["group"])
                user.groups.add(group)
                print(f"User {user.username} created and assigned to {group.name}.")
            else:
                print(f"User {user.username} already exists.")
