from django.conf import settings
from django.contrib import admin
from .models import Name,Id,Company,Information,Venue,Domain

# Register your models here.
admin.site.register(Name)
admin.site.register(Id)
admin.site.register(Company)
admin.site.register(Information)
admin.site.register(Domain)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )