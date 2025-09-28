from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def criar_grupos(sender, **kwargs):
    for nome in ['Administrador', 'Professor', 'Aluno']:
        Group.objects.get_or_create(name=nome)