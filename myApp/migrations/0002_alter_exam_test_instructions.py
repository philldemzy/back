# Generated by Django 4.0.4 on 2022-06-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='test_instructions',
            field=models.CharField(max_length=100),
        ),
    ]
