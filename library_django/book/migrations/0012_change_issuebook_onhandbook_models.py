# Generated by Django 4.2.2 on 2023-08-31 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0011_change_onhandbook_model"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="onhandbook",
            name="issuebook",
        ),
        migrations.AddField(
            model_name="issuebook",
            name="onhandbook",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="book.onhandbook",
            ),
        ),
    ]