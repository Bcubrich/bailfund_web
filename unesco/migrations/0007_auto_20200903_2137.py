# Generated by Django 3.1 on 2020-09-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0006_auto_20200903_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='justification',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='latitude',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.FloatField(max_length=20, null=True),
        ),
    ]
