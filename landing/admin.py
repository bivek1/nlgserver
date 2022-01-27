from django.contrib import admin
from .models import Branch, OtherDownload,Surveryor,CeoMessage, Agent, Citizen, Report,news, Download, fiscalYear
# Register your models here.
admin.site.register(Branch)
admin.site.register(OtherDownload)
admin.site.register(Surveryor)
admin.site.register(Agent)
admin.site.register(Citizen)
admin.site.register(Report)
admin.site.register(news)
admin.site.register(Download)
admin.site.register(fiscalYear)
admin.site.register(CeoMessage)
from .models import Bod, ManagementTeam, Setting, QuestionAnswer, Product, Sub_product, DepartmentHead
admin.site.register(Bod)
admin.site.register(ManagementTeam)
admin.site.register(Setting)
admin.site.register(QuestionAnswer)
admin.site.register(Product)
admin.site.register(Sub_product)
admin.site.register(DepartmentHead)