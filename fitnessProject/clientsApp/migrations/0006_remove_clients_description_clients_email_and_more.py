# Generated by Django 5.1.2 on 2024-10-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientsApp", "0001_squashed_0005_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clients",
            name="description",
        ),
        migrations.AddField(
            model_name="clients",
            name="email",
            field=models.EmailField(
                default="example@gmail.com", max_length=254, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="clients",
            name="client_age",
            field=models.IntegerField(),
        ),
    ]
