from django.contrib import admin
from .models import Branch, Surveryor, Agent, Citizen, Report,news, Download, fiscalYear
# Register your models here.
admin.site.register(Branch)
admin.site.register(Surveryor)
admin.site.register(Agent)
admin.site.register(Citizen)
admin.site.register(Report)
admin.site.register(news)
admin.site.register(Download)
admin.site.register(fiscalYear)