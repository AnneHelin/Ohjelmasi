from django.contrib import admin
from ...models import Kalenteri

admin.site.register(Kalenteri)
class kalenteriAdmin(admin.ModelAdmin):
    pass

