from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Benutzer
 
# Register your models here.


admin.site.site_header = "Zakria Application"
admin.site.index_title ="module"
admin.site.site_title= " Uni"



@admin.register(Benutzer)
class USERAdmin(admin.ModelAdmin):

    list_display= ("email",'first_name', "last_name", "date_joined",'role','is_active' )
    list_filter = ( "last_name", "date_joined",'role','is_active' )
    search_fields = ("date_joined",'role','is_active' )
    actions = ['aktivieren_status', 'deaktivieren_status']
    #list_filter = (AlphabetFilter,)

# with this method i get jsut the activ user in the list
    '''
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=True)
    '''

    def deaktivieren_status(self, request, queryset):
        return queryset.update(is_active=False)
    deaktivieren_status.short_description =(" User Deactivieren")

    def aktivieren_status(self, request, queryset):
        return queryset.update(is_active=True)
    aktivieren_status.short_description =(" User Aktivieren")
