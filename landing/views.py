from django.contrib import messages
from django.shortcuts import render
from .models import Branch, Agent, Download, Surveryor, Citizen, Report, Download, fiscalYear, news
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def landing(request):
    return render(request, "landing/index.html")

def productPolicy(request):
    return render(request, 'landing/products.html')

def aboutUs(request):
    return render(request, "landing/about.html")

def contact(request):
    return render(request, "landing/contactus.html")

def faq(request):
    return render(request, "landing/faq.html")

def term(request):
    return render(request, "landing/terms.html")

def training(request):
    return render(request, "landing/training.html")

def sitemap(request):
    return render(request, "landing/sitemap.html")


def finance(request):
    report = Report.objects.all()
    Yeara = fiscalYear.objects.all()
    media = settings.MEDIA_ROOT
    aa = media.replace('\\media',"")
    dist = {
        'rep':report,
        'aa':aa,
        'fis':Yeara
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
    return HttpResponseRedirect(reverse('landing:finance'))

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
    s = Surveryor.objects.all()
    dist = {
        's':s
    }
    return render(request, "landing/surveyor.html", dist)

def agents(request):
    s = Agent.objects.all()
    dist = {
        's':s
    }
    return render(request, "landing/agents.html", dist)

def citizen(request):
    s = Citizen.objects.all()
    dist = {
        's':s
    }
    return render(request, "landing/citizen.html", dist)

def branch(request):
    branch = Branch.objects.all().order_by('district')
    dist = {
        'branch':branch,
        'Nfound':False
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
            'Nfound':found
        }

        return render(request, 'landing/branch.html', distS)
    else:
        return render(request, 'landing/branch.html', dist)

def gallery(request):
    
    return render(request, "landing/gallary.html")

def download(request):
    d = news.objects.all()
    two = news.objects.all().order_by('-id')[:2]
    dist = {
        'd':d,
        'two': two
    }
    return render(request, "landing/download.html", dist)

def calculator(request):
    # return render(request, "landing/calculator/two_wheleer/twowheler_c.html")
    return render(request, "landing/calculator/twowheler.html")
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
    files = Download.objects.all()
    dist = {
        'files':files
    }
    return render(request, "landing/downloadfile.html", dist)


# Extra Calculator
def carCalculator(request):
    return render(request, 'landing/calculator/carCalculator.html')

def tempoCal(request):
    return render(request, 'landing/calculator/tempoCal.html')

def taxiCal(request):
    return render(request, 'landing/calculator/taxi.html')

def goodCal(request):
    return render(request, 'landing/calculator/goods.html')

def agriCal(request):
    return render(request, 'landing/calculator/agriculture.html')

def fuelTank(request):
    return render(request, 'landing/calculator/fuel.html')

def passenger(request):
    return render(request, 'landing/calculator/passenger.html')


def logIn(request):
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

    return render(request, "landing/login.html")