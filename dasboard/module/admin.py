from django.contrib import admin
from .models import Module, Owner


# Register your models here.


admin.site.site_header = "Zakria Application"
admin.site.index_title ="module"
admin.site.site_title= " Uni"

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):

    list_display= ("module_id", "module_id", "module_wahl",'martikelnummer')
    list_filter= ( "module_wahl",'martikelnummer')
    search_fields= ("module_id", "module_id", "module_wahl",'martikelnummer')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):

    list_display= ("owner_id",'email', "is_student", "salutation",'first_name','last_name','telephone','birthday' )
    list_filter = ("owner_id",'email', "is_student", "salutation",'first_name','last_name','telephone','birthday' )
    search_fields =("owner_id",'email', "is_student", "salutation",'first_name','last_name','telephone','birthday' )
