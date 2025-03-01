from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'accounts':  # Ensure this runs only for the accounts app
        content_type = ContentType.objects.get_for_model(CustomUser)

        
        permissions = {
            "can_view": "Can view records",
            "can_create": "Can create records",
            "can_edit": "Can edit records",
            "can_delete": "Can delete records",
        }

    
        groups = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_edit", "can_create", "can_delete"],
        }

        
        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                permission = Permission.objects.get(codename=perm_codename, content_type=content_type)
                group.permissions.add(permission)
