# Generated by Django 4.0.3 on 2022-04-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_randeveryday_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Randbored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(default='Solve aptitude problems; Comprehension; Fill in the blanks; Paint a picture; Cook recipies; Excerise; Draw what comes to your mind; ', max_length=1000)),
            ],
        ),
    ]
