from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('iqf_app', '0006_alter_iq_fiscalizados_inventarios_inventarios_id_and_more'),  # Reemplaza con la migración anterior
    ]

    operations = [
        migrations.RunSQL(
            sql='ALTER TABLE iqf_app_iq_fiscalizados_objetivos RENAME COLUMN `objetivos_id_id` TO `objetivos_id`;',
            reverse_sql='ALTER TABLE iqf_app_iq_fiscalizados_objetivos RENAME COLUMN `objetivos_id` TO `objetivos_id_id`;'
        ),
    ]
