# Generated by Django 3.0.7 on 2020-09-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booknview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='Price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]