# Generated by Django 3.0.6 on 2020-05-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_bookdatatwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdatatwo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]