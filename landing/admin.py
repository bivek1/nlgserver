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

from .models import Bod, ManagementTeam, Setting, QuestionAnswer, Product, Sub_product
admin.site.register(Bod)
admin.site.register(ManagementTeam)
admin.site.register(Setting)
admin.site.register(QuestionAnswer)
admin.site.register(Product)
admin.site.register(Sub_product)