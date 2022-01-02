from django.contrib import messages
from django.shortcuts import render
from .models import Announcement,Contact, Bod, Branch, Agent, DepartmentHead, Download, ManagementTeam, PageVisit, Product, QuestionAnswer, Setting, Surveryor, Citizen, Report, Download, fiscalYear, news
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def PageVisitView():
    PageVisit.objects.create(count = 1)

def landing(request):
    PageVisitView()
    sett = Setting.objects.all()
    ann = Announcement.objects.all()
    products = Product.objects.filter(hide=False)[:8]
    
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'ann':ann,
        'products':products,
        
    }
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['number'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        return HttpResponseRedirect(reverse('landing:landing'))
    return render(request, "landing/index.html", dist)

def productPolicy(request):
    PageVisitView()
    sett = Setting.objects.all()
    products = Product.objects.filter(hide=False).filter(discontinue= False)
    discontineu = Product.objects.filter(discontinue=True)
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'product':products,
        'discon':discontineu
    }
    return render(request, 'landing/products.html', dist)

def aboutUs(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'bod':Bod.objects.all(),
        'team':ManagementTeam.objects.all(),
        'depart':DepartmentHead.objects.all()
    }
    return render(request, "landing/about.html", dist)

def contact(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting
    }
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['number'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        messages.success(request,"Successfully Sent Message")
        return HttpResponseRedirect(reverse('landing:contact'))
    return render(request, "landing/contactus.html", dist)

def faq(request):
    PageVisitView()
    sett = Setting.objects.all()
    faq = QuestionAnswer.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'faq':faq
    }
    return render(request, "landing/faq.html", dist)

def term(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting
    }
    return render(request, "landing/terms.html", dist)

def training(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting
    }
    return render(request, "landing/training.html", dist)

def sitemap(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting
    }
    return render(request, "landing/sitemap.html", dist)


def finance(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break

    report = Report.objects.all()
    Yeara = fiscalYear.objects.all()
    media = settings.MEDIA_ROOT
    aa = media.replace('\\media',"")
    dist = {
        'rep':report,
        'aa':aa,
        'fis':Yeara,
        'setting':setting
    }
    return render(request, "landing/statement.html", dist)

def filedownload(request, slug, id):
    media = settings.MEDIA_ROOT
    # aa = media.replace('\\media',"")
    aa = media.replace('/media/',"")
    if slug == 'report':
        rep = Report.objects.get(id=id)
    elif slug=="news":
        rep = news.objects.get(id=id)
    else:
        rep = Download.objects.get(id = id)
    # file = open(aa+"/"+rep.files.url, "rb").read()
    file = open(aa+rep.files.url, "rb").read()
    rea_response = HttpResponse(file, content_type='application/pdf')
    rea_response['Content-Disposition'] = 'attachment; filename={}'.format(rep.name+'.pdf')
    return rea_response
    # return HttpResponseRedirect(reverse('landing:finance'))

def pdf_view(request,slug, id):
    media = settings.MEDIA_ROOT
    # aa = media.replace('\\media',"")
    aa = media.replace('/media/',"")
    if slug == 'report':
        rep = Report.objects.get(id=id)
    elif slug=="news":
        rep = news.objects.get(id=id)
    else:
        rep = Download.objects.get(id = id)
    print(media+"/"+rep.files.url)
    # file = open(aa+"/"+rep.files.url, "rb").read()
    file = open(aa+rep.files.url, "rb").read()
    try:
        # return FileResponse(open(aa+"/"+rep.files.url, 'rb'), content_type='application/pdf')
        return FileResponse(open(aa+rep.files.url, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def surveyor(request):
    PageVisitView()
    s = Surveryor.objects.all()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        's':s,
        'setting':setting
    }
    return render(request, "landing/surveyor.html", dist)

def agents(request):
    PageVisitView()
    s = Agent.objects.all()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        's':s,
        'setting':setting
    }

    return render(request, "landing/agents.html", dist)

def citizen(request):
    PageVisitView()
    s = Citizen.objects.all()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        's':s,
        'setting':setting
    }

    return render(request, "landing/citizen.html", dist)

def branch(request):
    PageVisitView()
    branch = Branch.objects.all().order_by('district')
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'branch':branch,
        'Nfound':False,
        'setting':setting
    }
    if request.method == 'POST':
        name = request.POST['branch']
        branch = Branch.objects.filter(Q(district__icontains=name) | Q(street__icontains=name))
        if branch:
            found= False
        else:
            found= True
        distS = {
            'branch':branch,
            'Nfound':found,
            'setting':setting
        }

        return render(request, 'landing/branch.html', distS)
    else:
        return render(request, 'landing/branch.html', dist)

def gallery(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
  
        'setting':setting
    }
    return render(request, "landing/gallary.html", dist)

def download(request):
    PageVisitView()
    d = news.objects.all()
    two = news.objects.all().order_by('-id')[:2]
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'd':d,
        'two': two,
        'setting':setting
    }
    return render(request, "landing/download.html", dist)

def calculator(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    # return render(request, "landing/calculator/two_wheleer/twowheler_c.html")
    return render(request, "landing/calculator/twowheler.html", dist)
def checkLogin(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
        data = {
            'status':'ok'
        }
        return JsonResponse(data)
    else:
        data = {
            'status':'error'
        }
        return JsonResponse(data)

def downloadFile(request):
    PageVisitView()
    files = Download.objects.all()
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'files':files,
        'setting':setting
    }
    return render(request, "landing/downloadfile.html", dist)




# Extra Calculator
def carCalculator(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/carCalculator.html', dist)

def tempoCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/tempoCal.html', dist)

def taxiCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/taxi.html', dist)

def goodCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/goods.html', dist)

def agriCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/agriculture.html', dist)

def fuelTank(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/fuel.html', dist)

def passenger(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/passenger.html', dist)


def tractor(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/tractor.html', dist)


def con(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/construction.html', dist)

def productCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/homecal.html', dist)


def propertyCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/propertycal.html', dist)


def personal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/personal.html', dist)

def agriCal(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    return render(request, 'landing/calculator/agri.html', dist)

def logIn(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'setting':setting
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse('manager:dashboard'))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect(reverse('landing:login'))

    return render(request, "landing/login.html", dist)

