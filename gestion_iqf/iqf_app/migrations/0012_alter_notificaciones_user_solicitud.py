# Generated by Django 4.2.3 on 2023-07-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iqf_app', '0011_notificaciones_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones_user',
            name='solicitud',
            field=models.FileField(blank=True, null=True, upload_to='solicitudes/'),
        ),
    ]
