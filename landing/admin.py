from django.contrib import admin
from .models import Branch, Term, OtherDownload,Surveryor,CeoMessage, Agent, Citizen, Report, TopBar,news, Download, fiscalYear
# Register your models here.
admin.site.register(Branch)
admin.site.register(OtherDownload)
admin.site.register(Surveryor)
admin.site.register(Agent)
admin.site.register(Citizen)
class CustomReport(admin.ModelAdmin):
    list_display = ('id','name','fiscal', 'rtype')
    list_display_links =None
    # readonly_fields = ('id',)
    list_editable =('id','name','fiscal', 'rtype')

admin.site.register(Report, CustomReport)
admin.site.register(Term)
admin.site.register(news)
admin.site.register(Download)

class CustomFiscalYear(admin.ModelAdmin):
    list_display = ('id','fiscal')
    list_display_links =None
    # readonly_fields = ('id',)
    list_editable =('id','fiscal')

admin.site.register(fiscalYear,CustomFiscalYear)
admin.site.register(CeoMessage)
from .models import Bod, ManagementTeam, Setting, QuestionAnswer, Product, Sub_product, DepartmentHead
admin.site.register(Bod)
admin.site.register(ManagementTeam)
admin.site.register(Setting)
admin.site.register(QuestionAnswer)
admin.site.register(Product)
admin.site.register(Sub_product)
admin.site.register(DepartmentHead)
admin.site.register(TopBar)