# Generated by Django 4.0.4 on 2022-06-08 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='mesaj içeriği')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='yeniden_app.room', verbose_name='Oda')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user', to='yeniden_app.room', verbose_name='Oda')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]