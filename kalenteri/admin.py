from django.contrib import admin
from kalenteri import models

@admin.register(models.Tapahtuma)
class TapahtumaAdmin(admin.ModelAdmin):
    model = models.Tapahtuma
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at"
    
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(models.Tapahtuma)
class Tapahtumakalenteri(admin.ModelAdmin):
    model = models.Tapahtuma
    list_display = ["id", "tapahtuma", "user", "created_at", "uppdated_at"]
    list_filter = ["tapahtuma"]