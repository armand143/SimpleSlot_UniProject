# Generated by Django 4.0.4 on 2022-06-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.IntegerField(choices=[(0, '08:00 – 10:00'), (1, '10:00 – 12:00'), (2, '12:00 – 14:00'), (3, '14:00 – 16:00'), (4, '16:00 – 18:00'), (5, '18:00 – 20:00')])),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_system', models.CharField(blank=True, choices=[('Art', 'Art'), ('Chemistry', 'Chemistry'), ('Technical Devices', 'Technical Devices'), ('Cooking', 'Cooking'), ('Music', 'Music')], max_length=30)),
                ('title', models.CharField(max_length=250)),
                ('Beschreibung', models.CharField(max_length=250)),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diction', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nutzer',
            fields=[
                ('matrikelnummer', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clus_name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.cluster')),
            ],
        ),
    ]
