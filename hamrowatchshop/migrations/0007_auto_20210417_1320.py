# Generated by Django 3.1.6 on 2021-04-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamrowatchshop', '0006_auto_20210402_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComingSoonWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('images', models.FileField(upload_to='static/uploads')),
            ],
        ),
        migrations.AlterField(
            model_name='hamrowatchshop',
            name='image',
            field=models.FileField(upload_to='static/uploads'),
        ),
    ]
