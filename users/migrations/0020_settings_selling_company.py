# Generated by Django 3.0.8 on 2020-11-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20201109_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='selling_company',
            field=models.BooleanField(default=False),
        ),
    ]