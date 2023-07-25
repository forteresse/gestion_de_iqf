# Generated by Django 4.2.3 on 2023-07-24 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iqf_app', '0012_alter_notificaciones_user_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='iq_fiscalizados_notificaciones_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iq_fiscalizados_id', models.ForeignKey(db_column='iq_fiscalizados_id', on_delete=django.db.models.deletion.CASCADE, to='iqf_app.iq_fiscalizados')),
                ('notificaciones_user_id', models.ForeignKey(db_column='notificaciones_user_id', on_delete=django.db.models.deletion.CASCADE, to='iqf_app.notificaciones_user')),
            ],
        ),
        migrations.AddField(
            model_name='notificaciones_user',
            name='iq_fiscalizado',
            field=models.ManyToManyField(through='iqf_app.iq_fiscalizados_notificaciones_user', to='iqf_app.iq_fiscalizados'),
        ),
    ]