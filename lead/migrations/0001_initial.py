# Generated by Django 4.2.1 on 2023-06-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Website', models.TextField()),
                ('Linkedin', models.TextField()),
                ('Industry', models.CharField(max_length=266)),
                ('Size', models.CharField(max_length=266)),
                ('Location', models.CharField(max_length=266)),
                ('Founded', models.CharField(max_length=266)),
                ('Description', models.TextField()),
                ('Company_Name', models.TextField()),
                ('IP_adresse', models.TextField()),
                ('IP_country', models.TextField()),
                ('Email', models.TextField()),
                ('Phones', models.TextField()),
                ('Title', models.TextField()),
                ('Description_W', models.TextField()),
                ('Language', models.TextField()),
                ('Verification_Date', models.TextField()),
                ('Copyright_year', models.TextField()),
                ('Copyright_owner', models.TextField()),
                ('responsiveOrNot', models.TextField()),
                ('Issuer', models.TextField()),
                ('Cert_Country', models.TextField()),
                ('Cert_state', models.TextField()),
                ('Cert_Locality', models.TextField()),
                ('Serial_number', models.TextField()),
                ('Cert_start_date', models.TextField()),
                ('Cert_expiry', models.TextField()),
                ('SSL_TLS', models.TextField()),
                ('Cert_Protocol', models.TextField()),
                ('Cert_Organization', models.TextField()),
                ('Schema_type', models.TextField()),
                ('GoogleAnalytics_ID', models.TextField()),
                ('AdSense_ID', models.TextField()),
                ('Spf_record', models.TextField()),
                ('Dmarc_record', models.TextField()),
                ('Facebook', models.TextField()),
                ('Twitter', models.TextField()),
                ('Linkedin_W', models.TextField()),
                ('Instagram', models.TextField()),
                ('Youtube', models.TextField()),
                ('Owler', models.TextField()),
                ('Pintrest', models.TextField()),
                ('Skype', models.TextField()),
                ('WhatsApp', models.TextField()),
            ],
        ),
    ]