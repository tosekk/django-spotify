# Generated by Django 4.0.3 on 2022-04-26 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_alter_usermodel_is_newsletter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name_plural': 'Users'},
        ),
    ]
