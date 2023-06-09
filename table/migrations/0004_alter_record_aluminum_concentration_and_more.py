# Generated by Django 4.2 on 2023-05-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_record_delete_entries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='aluminum_concentration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='calcium_concentration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='iron_concentration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='silicon_concentration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='sulfur_concentration',
            field=models.FloatField(),
        ),
    ]
