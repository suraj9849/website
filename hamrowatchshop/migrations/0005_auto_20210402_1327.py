# Generated by Django 3.1.6 on 2021-04-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamrowatchshop', '0004_auto_20210401_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamrowatchshop',
            name='image',
            field=models.ImageField(upload_to='static/uploads'),
        ),
    ]
