# Generated by Django 4.2.3 on 2023-07-27 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iqf_app', '0021_notificaciones_user_nro_oficio'),
    ]

    operations = [
        migrations.CreateModel(
            name='reporte_actualizacion',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='iq_fiscalizados',
            name='reporte_actualizacion_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iqf_app.reporte_actualizacion'),
        ),
    ]