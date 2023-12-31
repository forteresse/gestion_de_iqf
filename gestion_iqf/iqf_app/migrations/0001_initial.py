# Generated by Django 4.2.3 on 2023-07-16 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='areas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='escuelas',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='inventarios',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('condicion', models.BooleanField()),
                ('auth_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('escuelas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iqf_app.escuelas')),
            ],
        ),
        migrations.CreateModel(
            name='facultades',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('areas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iqf_app.areas')),
            ],
        ),
        migrations.AddField(
            model_name='escuelas',
            name='facultades_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iqf_app.facultades'),
        ),
    ]
