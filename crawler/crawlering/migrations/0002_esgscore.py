# Generated by Django 4.0.5 on 2022-06-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EsgScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.CharField(max_length=500)),
                ('Rank', models.CharField(max_length=500)),
                ('Environment', models.CharField(max_length=500)),
                ('Social', models.CharField(max_length=500)),
                ('Governance', models.CharField(max_length=500)),
            ],
        ),
    ]