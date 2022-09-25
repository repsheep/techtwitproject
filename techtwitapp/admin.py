from django.contrib import admin

from .models import RecordPost

class RecordPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
    
    
admin.site.register(RecordPost, RecordPostAdmin)

