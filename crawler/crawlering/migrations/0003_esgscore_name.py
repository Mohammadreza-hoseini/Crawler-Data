# Generated by Django 4.0.5 on 2022-06-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlering', '0002_esgscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='esgscore',
            name='name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]