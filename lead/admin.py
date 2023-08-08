from django.contrib import admin
from .models import lead
# Register your models here.


class leadAdmin(admin.ModelAdmin):
    #list_display = ('amount', 'description', 'owner', 'category', 'date',)
    list_display = ('Website', 'Linkedin', 'Industry', 'Size', 'Location', 'Founded', 'Description', 'Company_Name', 'IP_adresse', 'IP_country', 'Email',
                    'Phones', 'Title', 'Description_W', 'Language', 'Verification_Date', 'Copyright_year', 'Copyright_owner', 'responsiveOrNot', 'Issuer',
                    'Cert_Country', 'Cert_state', 'Cert_Locality', 'Serial_number', 'Cert_start_date', 'Cert_expiry', 'SSL_TLS', 'Cert_Protocol', 
                    'Cert_Organization', 'Schema_type', 'GoogleAnalytics_ID', 'AdSense_ID', 'Spf_record', 'Dmarc_record', 'Facebook', 'Twitter',
                    'Linkedin_W', 'Instagram', 'Youtube', 'Owler', 'Pintrest', 'Skype', 'WhatsApp')

    search_fields = ('Industry', 'Size', 'Location', 'Founded','Company_Name',)

    list_per_page = 5


admin.site.register(lead, leadAdmin)
#admin.site.register(Category)
