# Generated by Django 4.1.2 on 2022-11-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jp', upload_to='images/'),
        ),
    ]
