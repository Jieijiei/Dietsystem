# Generated by Django 3.0.4 on 2020-06-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0002_weight_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='bmi',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='weight',
            name='himando',
            field=models.CharField(default='', max_length=50),
        ),
    ]
