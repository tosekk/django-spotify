# Generated by Django 4.0.3 on 2022-04-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=60)),
                ('user_birthdate', models.DateField()),
                ('user_gender', models.CharField(max_length=10)),
                ('is_newsletter', models.BooleanField()),
            ],
        ),
    ]