# Generated by Django 3.0.7 on 2020-09-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('From', models.CharField(max_length=50)),
                ('To', models.CharField(max_length=50)),
            ],
        ),
    ]
