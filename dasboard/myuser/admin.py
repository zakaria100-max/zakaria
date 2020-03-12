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
