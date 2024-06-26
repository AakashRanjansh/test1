# Generated by Django 4.2 on 2023-04-27 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('number_of_people', models.IntegerField()),
                ('event_date', models.DateField()),
                ('event_location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/services/')),
                ('rank', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/plans/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subhakaarya_app.service', to_field='title')),
            ],
        ),
        migrations.CreateModel(
            name='EventPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_people', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subhakaarya_app.event')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subhakaarya_app.plan')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='plans',
            field=models.ManyToManyField(through='subhakaarya_app.EventPlan', to='subhakaarya_app.plan'),
        ),
    ]
