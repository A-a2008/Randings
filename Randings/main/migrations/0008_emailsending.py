# Generated by Django 4.0.3 on 2022-04-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_asked'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
            ],
        ),
    ]
