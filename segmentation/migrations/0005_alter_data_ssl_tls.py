# Generated by Django 4.2.1 on 2023-07-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segmentation', '0004_data_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='SSL_TLS',
            field=models.CharField(choices=[('Enabled', 'Enabled'), ('Not Enabled', 'Not Enabled'), ('NO', 'N/A')], default='NO', max_length=100),
        ),
    ]