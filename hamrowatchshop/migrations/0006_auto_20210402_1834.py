# Generated by Django 3.1.6 on 2021-04-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamrowatchshop', '0005_auto_20210402_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamrowatchshop',
            name='image',
            field=models.CharField(max_length=2000),
        ),
    ]
