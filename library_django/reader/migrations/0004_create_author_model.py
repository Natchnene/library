# Generated by Django 4.2.4 on 2023-08-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reader", "0003_change_user_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_name_number",
            field=models.CharField(max_length=250, unique=True, verbose_name="last name - unique number"),
        ),
    ]
