# Generated by Django 3.2.10 on 2022-03-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_is_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
