# Generated by Django 4.2.3 on 2023-07-26 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iqf_app', '0019_remove_perfil_usuario_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil_usuario',
            name='titulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='iqf_app.titulos'),
        ),
    ]
