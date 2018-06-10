from django.contrib import admin


from .models import Line, Train, CleanRecords

admin.site.register(Line)
admin.site.register(Train)
admin.site.register(CleanRecords)
