from django.contrib import admin
from.models import ForeastShortTerm, ForecastLongTerm
# Register your models here

class ForecastShortTermAdmin(admin.ModelAdmin):
	list_display = ('date', 'user')
	ordering = ['-date']

class ForecastLongTermAdmin(admin.ModelAdmin):
	list_display = ('date', 'user')
	ordering = ['-date']

admin.site.register(ForeastShortTerm, ForecastShortTermAdmin)
admin.site.register(ForecastLongTerm, ForecastLongTermAdmin)