# Generated by Django 3.1 on 2020-09-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ideas', '0002_auto_20200905_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
