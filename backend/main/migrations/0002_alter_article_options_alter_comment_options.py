# Generated by Django 4.0.3 on 2022-08-07 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date',)},
        ),
    ]
