# Generated by Django 4.2.2 on 2023-07-04 09:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47d34785-837c-4f1d-9a89-951173b379a4'), primary_key=True, serialize=False),
        ),
    ]