# Generated by Django 5.0.1 on 2024-02-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_alter_customer_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="profile_pic",
            field=models.ImageField(
                blank=True, default="imgs/defaultProfile.png", null=True, upload_to=""
            ),
        ),
    ]
