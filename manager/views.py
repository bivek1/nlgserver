from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import AgentF, AnnouncementForm, BranchF, DepartmentHeadForm, DownloadForm, SettingForm, SurveryorF, CitizenF, ReportF, newsF, BodForm, ManagementForm, ProductFrom, SubProductFrom, QuestionAnswerFrom
from landing.models import Announcement, Branch, DepartmentHead, PageVisit, Setting, news, Surveryor, Agent, Citizen, Report, Download, Bod, ManagementTeam, Product, Sub_product, QuestionAnswer
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
@login_required
def dashboard(request):
    news_count = news.objects.all().count()
    branch_count = Branch.objects.all().count()
    agent_count = Agent.objects.all().count()
    citizen_count = Citizen.objects.all().count()
    report_count = Report.objects.all().count()
    survey_count = Surveryor.objects.all().count()
    product_count = Product.objects.all().count()
    sub_product_count = Sub_product.objects.all().count()
    faq_count = QuestionAnswer.objects.all().count()
    form_count = Download.objects.all().count()
    depart_count = DepartmentHead.objects.all().count()
    bod_count = Bod.objects.all().count()
    manage_count = ManagementTeam.objects.all().count()
    page_count = PageVisit.objects.all().count()
    
    
    dist ={
        'news_count':news_count,
        'branch_count':branch_count,
        'agent_count':agent_count,
        'citizen_count': citizen_count,
        'report_count':report_count,
        'survey_count':survey_count,
        'product_count':product_count,
        'sub_product_count':sub_product_count,
        'faq_count':faq_count,
        'form_count':form_count,
        'depart_count':depart_count,
        'bod_count':bod_count,
        'manage_count':manage_count,
        'count':page_count
        }
    return render(request, "manager/dashboard.html", dist)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing:landing'))
    
    
def addAgent(request):
    form = AgentF(request.POST or None)
    agent = Agent.objects.all().order_by('-id')
    dist = {
        'form':form,
        'data':agent
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Agents Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addAgent'))
    else:
        return render(request, 'manager/addAgent.html',dist )
       
    return render(request, 'manager/addAgent.html',dist )


def addBranch(request):
    form = BranchF()
    branched = Branch.objects.all().order_by('district')
    dist = {
        'form':form,
        'branch':branched,
    }
    if request.method == 'POST':
        form = BranchF(request.POST, request.FILES or None)
        if form.is_valid():        
            form.save()
            messages.success(request, "Branch Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:addBranch'))
        else:
            return render(request, 'manager/addBranch.html',dist )
    else:
        return render(request, 'manager/addBranch.html',dist )

def deleteBranch(request, id):
    branch = Branch.objects.get(id = id)
    branch.delete()
    messages.success(request, "Successfully Deleted Branch")
    return HttpResponseRedirect(reverse('manager:addBranch'))


def addSurveryor(request):
    form = SurveryorF(request.POST or None)
    agent = Surveryor.objects.all().order_by('-id')
    dist = {
        'form':form,
        'data':agent
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Surveryor Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addSurveryor'))
    else:
        return render(request, 'manager/addSurveryor.html',dist )
       
    return render(request, 'manager/addSurveryor.html',dist )


def addCitizen(request):
    form = CitizenF(request.POST or None)
    agent = Citizen.objects.all().order_by('-id')
    dist = {
        'form':form,
        'data':agent
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Citizen Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addCitizen'))
    else:
        return render(request, 'manager/addCitizen.html',dist )
       
    return render(request, 'manager/addCitizen.html',dist )

def addNews(request):
    form = newsF()
    dist = {
        'form':form
    }
    if request.method == 'POST':
        forms = newsF(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "News Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:addNews'))
        else:
            messages.error(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:addNews'))
    else:
        return render(request, 'manager/addNews.html',dist )
       

def addReport(request):
    form = ReportF()
    dist = {
        'form':form
    }
    if request.method == 'POST':
        forms = ReportF(request.POST, request.FILES)
        if forms.is_valid():
        
            forms.save()
            messages.success(request, "Report Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:addReport'))
        else:
            messages.success(request, "Something went Wrong")
            return render(request, 'manager/addReport.html',dist )
    else:
        return render(request, 'manager/addReport.html',dist )


def formReport(request, id):
    if id == 1:
        report = Download.objects.filter(dtype = 'KYC Form').order_by("-id")
        name = "KYC Form"
    elif id == 2:
        report = Download.objects.filter(dtype = 'Proposal Form').order_by("-id")
        name = "Proposal Form"
    else:
        report = Download.objects.filter(dtype = 'Claim Form').order_by("-id")
        name = "Claim Form"

    dist ={
        'name':name,
        'report':report,
        'type':id
    }
    return render(request, 'manager/viewForm.html', dist)

def statementReport(request, id):
    if id == 1:
        report = Report.objects.filter(rtype = 'Annual Report').order_by("-id")
        name = "Annual Report"
    elif id == 2:
        report = Report.objects.filter(rtype = 'Quarterly Report').order_by("-id")
        name = "Quarterly Report"
    elif id == 3:
        report = Report.objects.filter(rtype = 'Minute Report').order_by("-id")
        name = "Minute Report"
    else:
        report = Report.objects.filter(rtype = 'Other Report').order_by("-id")
        name = "Other Report"

    dist ={
        'name':name,
        'report':report,
        'type':id
    }
    return render(request, 'manager/viewReport.html', dist)

def newUpdate(request):
    report = news.objects.all().order_by("-id")
    name = "News and Update"

    dist ={
        'name':name,
        'report':report
    }
    return render(request, 'manager/news.html', dist)

def setting(request):
    sett = Setting.objects.all()
    form = SettingForm()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
        form.fields['email'].initial = setting.email
        form.fields['number1'].initial = setting.number1
        form.fields['number2'].initial = setting.number2
        form.fields['location'].initial = setting.location
        form.fields['toll_free_no'].initial = setting.toll_free_no

    dist = {
        'setting':setting,
        'form':form
    }
    if request.method == 'POST':
        form = SettingForm(request.POST, request.FILES)
        if form.is_valid():
            
            if sett:
                setting.email = request.POST['email']
                setting.number1 = request.POST['number1']
                setting.number2 = request.POST['number2']
                setting.location = request.POST['location']
                setting.toll_free_no = request.POST['toll_free_no']
                try:
                   setting.logo = request.FILES['logo']
                except:
                    pass
                setting.save()
            else:
                form.save()
            messages.success(request, "Successfully Updated Settings")
            return HttpResponseRedirect(reverse("manager:setting"))
    else:
        return render(request, "manager/settings.html", dist)


def addBod(request):
    form = BodForm()
    branched = Bod.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        form = BodForm(request.POST, request.FILES or None)
        if form.is_valid():        
            form.save()
            messages.success(request, "Bod Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:addBod'))
        else:
            messages.success(request, "Something went Wrong")
            return render(request, 'manager/addBod.html',dist )
    else:
        return render(request, 'manager/addBod.html',dist )

def managementTeam(request):
    form = ManagementForm()
    branched = ManagementTeam.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        form = ManagementForm(request.POST, request.FILES or None)
        if form.is_valid():        
            form.save()
            messages.success(request, "Management Team Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:managementTeam'))
        else:
            messages.success(request, "Something went Wrong")
            return render(request, 'manager/managementTean.html',dist )
    else:
        return render(request, 'manager/managementTean.html',dist )


def ProductView(request):
    form = ProductFrom()
    branched = Product.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        form = ProductFrom(request.POST, request.FILES or None)
        if form.is_valid():        
            form.save()
            messages.success(request, "Product Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:product'))
        else:
            messages.success(request, "Something went Wrong")
            return render(request, 'manager/product.html',dist )
    else:
        return render(request, 'manager/product.html',dist )
    

def SubProductView(request):
    form = SubProductFrom()
    branched = Sub_product.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        form = SubProductFrom(request.POST, request.FILES or None)
        if form.is_valid():        
            form.save()
            messages.success(request, "Sub Product Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:subProduct'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:subProduct'))
    else:
        return render(request, 'manager/sub_product.html',dist )


def QuestionAnswerView(request):
    form = QuestionAnswerFrom()
    branched = QuestionAnswer.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        form = QuestionAnswerFrom(request.POST)
        if form.is_valid():        
            form.save()
            messages.success(request, "Question Answer Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:questionAnswer'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:questionAnswer'))
    else:
        return render(request, 'manager/questionAnswer.html',dist )

def AnnouncementView(request):
    form = AnnouncementForm()
    branched = Announcement.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():        
            form.save()
            messages.success(request, "Announcement Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:announcement'))
        else:
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('manager:announcement'))
    else:
        return render(request, 'manager/announcement.html',dist )


def addForm(request):
    form = DownloadForm()

    dist = {
        'form':form,
    }
    if request.method == 'POST':
        forms = DownloadForm(request.POST, request.FILES)
        if forms.is_valid():        
            forms.save()
            messages.success(request, "Forms Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:addForm'))
        else:
            messages.success(request, "Something went Wrong")
            return render(request, 'manager/addForm.html',dist )
    else:
        return render(request, 'manager/addForm.html',dist)


def DepartmentView(request):
    form = DepartmentHeadForm()
    branched = DepartmentHead.objects.all()
    dist = {
        'form':form,
        'bod':branched,
    }
    if request.method == 'POST':
        forms = DepartmentHeadForm(request.POST, request.FILES or None)
        if forms.is_valid():        
            forms.save()
            messages.success(request, "Department Team Saved Succesfully")
            return HttpResponseRedirect(reverse('manager:departmentTeam'))
        else:
            messages.success(request, "Something went Wrong")
            return render(request, 'manager/departmentTeam.html',dist )
    else:
        return render(request, 'manager/departmentTeam.html',dist )

def deleteAnn(request, id):
    aa=  Announcement.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Announcement")
    return HttpResponseRedirect(reverse('manager:announcement'))

def deleteProduct(request, id):
    aa=  Product.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Product")
    return HttpResponseRedirect(reverse('manager:product'))

def deleteSubProduct(request, id):
    aa =  Sub_product.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Sub-Product")
    return HttpResponseRedirect(reverse('manager:subProduct'))

def deleteQuestion(request, id):
    aa =  QuestionAnswer.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Questions")
    return HttpResponseRedirect(reverse('manager:questionAnswer'))

def deleteDepartment(request, id):
    aa =  DepartmentHead.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Department Team")
    return HttpResponseRedirect(reverse('manager:departmentTeam'))


def deleteAgent(request, id):
    aa =  Agent.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Agent")
    return HttpResponseRedirect(reverse('manager:addAgent'))

def deleteCitizen(request, id):
    aa =  Citizen.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Citizen")
    return HttpResponseRedirect(reverse('manager:addCitizen'))

def deleteSuveryor(request, id):
    aa =  Surveryor.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Surveryor")
    return HttpResponseRedirect(reverse('manager:addSurveryor'))

def deleteBod(request, id):
    aa =  Bod.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Bod")
    return HttpResponseRedirect(reverse('manager:addBod'))

def deleteManagement(request, id):
    aa =  ManagementTeam.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Management Team")
    return HttpResponseRedirect(reverse('manager:managementTeam'))

def deleteReport(request, id, type):
    aa =  Report.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Report")
    return HttpResponseRedirect(reverse('manager:statementReport', args=[type]))

def deleteForm(request, id, type):
    aa =  Download.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted Forms")
    return HttpResponseRedirect(reverse('manager:formReport', args=[type]))

def deleteNews(request, id):
    aa =  news.objects.get(id =id )
    aa.delete()
    messages.success(request,"Sucessfully Deleted News")
    return HttpResponseRedirect(reverse('manager:newUpdate'))