from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('industry', 'location', 'size', 'founded','Count_Analytics', 'Count_records','Count_contact', 'Expiry_status','ResponsiveOrNot','SSL_TLS','predictions')


admin.site.register(Data, DataAdmin)
