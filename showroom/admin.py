from django.contrib import admin
from .models import *
# Register your models here.

class ShowroomAdmin(admin.ModelAdmin):
    list_display = ("name","location")
    list_display_links = ("name",)

admin.site.register(Showroom,ShowroomAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ("name","role","contact_number","email")
    list_display_links = ("name","email")

admin.site.register(Team,TeamAdmin)


class BrandsAdmin(admin.ModelAdmin):
    list_display = ("name","country")
    list_display_links = ("name",)

admin.site.register(Brands,BrandsAdmin)


class EngineAdmin(admin.ModelAdmin):
    list_display = ("engine_type","power","engine_number")
    list_display_links = ("engine_type",)

admin.site.register(Engine,EngineAdmin)



class ModelsAdmin(admin.ModelAdmin):
    list_display = ("name","brand","engine")
    list_display_links = ("name","brand")

admin.site.register(Models,ModelsAdmin)



class FeaturesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)

admin.site.register(Features,FeaturesAdmin)