# Generated by Django 4.1.7 on 2023-02-28 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauth',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oauth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='oauth',
            constraint=models.UniqueConstraint(fields=('uid', 'provider_type'), name='unique_OAuth2_as_uid_and_provider_type'),
        ),
    ]