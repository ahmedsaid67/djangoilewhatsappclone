# Generated by Django 4.0.4 on 2022-06-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeniden_app', '0002_room_first_user_room_second_user_delete_chatuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
