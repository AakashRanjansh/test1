# Generated by Django 4.2 on 2023-06-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='phone',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
    ]
