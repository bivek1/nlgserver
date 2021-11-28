from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import AgentF, BranchF, SurveryorF, CitizenF, ReportF, newsF
from landing.models import Branch, news, Surveryor, Agent, Citizen, Report, Download
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

    
    dist ={
        'news_count':news_count,
        'branch_count':branch_count,
        'agent_count':agent_count,
        "citizen_count": citizen_count,
        'report_count':report_count,
        'survey_count':survey_count,

    }
    return render(request, "manager/dashboard.html", dist)

def logoutUser(request):
    logout(request)
    
    return render(request, "landing/index.html")
    
    
def addAgent(request):
    form = AgentF(request.POST or None)
    dist = {
        'form':form
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Agents Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addAgent'))
    else:
        return render(request, 'manager/addAgent.html',dist )
       
    return render(request, 'manager/addAgent.html',dist )


def addBranch(request):
    form = BranchF(request.POST or None)
    dist = {
        'form':form
    }

    if form.is_valid():
        form = BranchF(request.POST, request.FILES or None)
        form.save()
        messages.success(request, "Branch Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addBranch'))
    else:
        return render(request, 'manager/addBranch.html',dist )
       
    return render(request, 'manager/addBranch.html',dist )


def addSurveryor(request):
    form = SurveryorF(request.POST or None)
    dist = {
        'form':form
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
    dist = {
        'form':form
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Citizen Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addCitizen'))
    else:
        return render(request, 'manager/addCitizen.html',dist )
       
    return render(request, 'manager/addCitizen.html',dist )

def addNews(request):
    form = newsF(request.POST, request.FILES or None)
    dist = {
        'form':form
    }
    if form.is_valid():
    
        form.save()
        messages.success(request, "News Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addNews'))
    else:
        return render(request, 'manager/addNews.html',dist )
       
    return render(request, 'manager/addNews.html',dist )

def addReport(request):
    form = ReportF(request.POST, request.FILES or None)
    dist = {
        'form':form
    }
    if form.is_valid():
    
        form.save()
        messages.success(request, "Report Saved Succesfully")
        return HttpResponseRedirect(reverse('manager:addReport'))
    else:
        return render(request, 'manager/addReport.html',dist )
       
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
        'report':report
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
        'report':report
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