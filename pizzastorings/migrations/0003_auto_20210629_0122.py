# Generated by Django 2.2.24 on 2021-06-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzastorings', '0002_auto_20210626_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='ontoppings',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizzasize',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizzatype',
        ),
        migrations.AddField(
            model_name='pizza',
            name='sizes',
            field=models.CharField(default=' ', max_length=50, verbose_name='Size of Pizza'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.CharField(default=' ', max_length=200, verbose_name='Toppings'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='type',
            field=models.CharField(default=' ', max_length=20, verbose_name='Type of Pizza'),
        ),
    ]
