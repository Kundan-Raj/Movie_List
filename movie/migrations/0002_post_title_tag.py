# Generated by Django 3.1.2 on 2020-10-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Freking Awsome Movies !!', max_length=100),
        ),
    ]
