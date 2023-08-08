# Generated by Django 4.2.1 on 2023-07-11 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(default='N/A', max_length=100)),
                ('location', models.CharField(default='N/A', max_length=100)),
                ('size', models.PositiveIntegerField(default='N/A')),
                ('founded', models.PositiveIntegerField(default='N/A', validators=[django.core.validators.MinValueValidator(1500), django.core.validators.MaxValueValidator(2023)])),
                ('verification', models.PositiveIntegerField(choices=[('Not verified', 0), ('Verified', 1)], default='Not verified')),
                ('Count_Analytics', models.PositiveIntegerField(choices=[(0, 'No IDs'), (1, 'One ID'), (2, 'Tow IDs'), (3, 'more than 2')], null=True)),
                ('Count_records', models.PositiveIntegerField(choices=[(0, 'No records'), (1, 'SPF or Dmarc'), (2, 'SPF and Dmarc')], null=True)),
                ('Count_contact', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('Expiry_status', models.CharField(choices=[('Expired', 'Expired'), ('Not Expired', 'Not Expired'), ("Don't know", 'N/A')], default="Don't know", max_length=100)),
                ('ResponsiveOrNot', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", 'N/A')], default="Don't know", max_length=10)),
                ('SSL_TLS', models.CharField(choices=[('Enabled', 'Enabled'), ('NO', 'N/A')], default='NO', max_length=10)),
                ('predictions', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]