# Generated by Django 4.2.3 on 2023-07-27 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iqf_app', '0022_reporte_actualizacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='iq_fiscalizados_pecosas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pecosas',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('pecosa_pdf', models.FileField(upload_to='pecosas/')),
            ],
        ),
        migrations.RemoveField(
            model_name='iq_fiscalizados',
            name='reporte_actualizacion_id',
        ),
        migrations.AlterField(
            model_name='notificaciones_user',
            name='fecha_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='reporte_actualizacion',
        ),
        migrations.AddField(
            model_name='iq_fiscalizados_pecosas',
            name='iq_fiscalizados_id',
            field=models.ForeignKey(blank=True, db_column='iq_fiscalizados_id', on_delete=django.db.models.deletion.CASCADE, to='iqf_app.iq_fiscalizados'),
        ),
        migrations.AddField(
            model_name='iq_fiscalizados_pecosas',
            name='pecosas_id',
            field=models.ForeignKey(blank=True, db_column='pecosas_id', on_delete=django.db.models.deletion.CASCADE, to='iqf_app.pecosas'),
        ),
        migrations.AddField(
            model_name='iq_fiscalizados',
            name='pecosas',
            field=models.ManyToManyField(through='iqf_app.iq_fiscalizados_pecosas', to='iqf_app.pecosas'),
        ),
    ]