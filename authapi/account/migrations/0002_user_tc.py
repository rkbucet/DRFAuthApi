# Generated by Django 4.0.3 on 2024-01-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tc',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
