# Generated by Django 3.0.8 on 2020-08-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='link_to_forum_post',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='receipt_paste_text',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='trade_list_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]