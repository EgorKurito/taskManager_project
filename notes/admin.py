from django.contrib import admin

from . import models


class NoteModelAdmin(admin.ModelAdmin):
    list_display = ["title", "publish", "updated", "category", "favourite"]
    list_filter = ["publish", "updated", "category", "favourite"]
    ordering = ['publish']
    list_display_links = ["publish", "updated", "category", "favourite"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta:
        model = models.Note

admin.site.register(models.Note, NoteModelAdmin)
admin.site.register(models.Category)
