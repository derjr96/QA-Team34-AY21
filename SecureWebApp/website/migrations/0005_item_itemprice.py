# Generated by Django 3.2.3 on 2021-10-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20211019_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemPrice',
            field=models.FloatField(default='0', max_length=10),
        ),
    ]
