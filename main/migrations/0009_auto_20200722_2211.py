# Generated by Django 3.0.8 on 2020-07-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_item_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='listing',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]