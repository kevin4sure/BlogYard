# Generated by Django 2.1 on 2019-03-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='picture',
            field=models.ImageField(upload_to='user_pic'),
        ),
    ]