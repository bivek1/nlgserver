
from django.contrib import messages
from django.shortcuts import render
from .models import Announcement, CeoMessage,Contact, Bod, Branch, Agent, DepartmentHead, Download, ManagementTeam, OtherDownload, PageVisit, Product, QuestionAnswer, RIpartner, Setting, Sub_product, Surveryor, Citizen, Report, Download, TopBar, fiscalYear, helpCenter, news, socialSite
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import get_template
# Create your views here.


def PageVisitView():
    PageVisit.objects.create(count = 1)

def landing(request):
    PageVisitView()
    sett = Setting.objects.all()
    ann = Announcement.objects.all()
    products = Product.objects.filter(hide=False).order_by('ordering')[:8]
    setting = None
    message = CeoMessage.objects.all()
    if messages:
        for i in message:
            msg = i.message
            break
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'ann':ann,
        'products':products,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all(),
        'msg':msg
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            subject = subject,
            message = message,
        )
        email_from = settings.EMAIL_HOST_USER
        contx = {
            'name':name,
            'number':phone,
            'email':email,
            'subject':subject,
            'message':message
        }
      
        email_from = settings.EMAIL_HOST_USER
        try:
            message = get_template('contact.html').render(contx)
            msg = EmailMessage(
                'Subject',
                message,
                email_from,
                [setting.email],
            )
            msg.content_subtype ="html"# Main content is now text/html
            msg.send()
            messages.success(request,"Successfully Sent Message")
        except:
            messages.success(request,"Fail Sending Mail")
        # real_msg = "Name: "+str(name)+ " I would like to get contact  "+ ". Number: " + str(phone) + ". Email: " +str(email) + " Message: " + str(message)
        # try:
        #     send_mail(subject, real_msg, email_from, [setting.email] , fail_silently=False,)
        #     messages.success(request,"Successfully Sent Message")
        # except:
        #     messages.success(request,"Fail Sending Mail")
        return HttpResponseRedirect(reverse('landing:landing'))
    return render(request, "landing/index.html", dist)

def productPolicy(request):
    PageVisitView()
    sett = Setting.objects.all()
    topP = Product.objects.filter(hide=False).filter(discontinue= False).order_by('ordering')[:8]
    products = Product.objects.filter(hide=False).filter(discontinue= False).order_by('ordering')
    allSub = Sub_product.objects.filter(hide=False).filter(discontinue= False)
    lens = products.count()
    discontineu = Product.objects.filter(discontinue=True)
    setting = None
    for i in topP:
        showm = i.id
        break
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'product':products,
        'discon':discontineu,
        'lens':lens,
        'topP':topP,
        'showm':showm,
        'allSub':allSub,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    return render(request, 'landing/products.html', dist)

def aboutUs(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    msg = None
    message = CeoMessage.objects.all()
    riartner = RIpartner.objects.all()
    ri = None
    for i in riartner:
        ri = i
        break
    if messages:
        for i in message:
            msg = i.message
            break
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'bod':Bod.objects.all().order_by('ordering'),
        'msg':msg,
        'team':ManagementTeam.objects.all().order_by('ordering'),
        'depart':DepartmentHead.objects.all().order_by('ordering'),
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all(),
        'ri': ri
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            subject = subject,
            message = message,
        )
        contx = {
            'name':name,
            'number':phone,
            'email':email,
            'subject':subject,
            'message':message
        }
      
        email_from = settings.EMAIL_HOST_USER
        try:
            message = get_template('contact.html').render(contx)
            msg = EmailMessage(
                'Subject',
                message,
                email_from,
                [setting.email],
            )
            msg.content_subtype ="html"# Main content is now text/html
            msg.send()
            messages.success(request,"Successfully Sent Message")
        except:
            messages.success(request,"Fail Sending Mail")

        # real_msg = "Name: "+str(name)+ " I would like to get contact  "+ ". Number: " + str(phone) + ". Email: " +str(email) + " Message: " + str(message)
        # try:
        #     send_mail(subject, real_msg, email_from, [setting.email] , fail_silently=False,)
        #     messages.success(request,"Successfully Sent Message")
        # except:
        #     messages.success(request,"Fail Sending Mail")
        return HttpResponseRedirect(reverse('landing:contact'))
    return render(request, "landing/contactus.html", dist)
def helpCen(request):
    
    setting = None
    sett = Setting.objects.all()
    name = None
    fas = None
    if sett:
        for i in sett:
            setting = i 
            break
    das = helpCenter.objects.all().order_by('-id')
    for i in das:
        name = i.id
        break
    data = helpCenter.objects.all().order_by('-id').exclude(id=name)
    fa = QuestionAnswer.objects.all().order_by('ordering')
    for i in fa:
        fas = i.id
        break
    print(name)
    dist = {
        'data':data,
        'show':helpCenter.objects.get(id = name),
        'faq': fa,
        'fas':fas,
        'bar':TopBar.objects.all(),
        'setting':setting,
        'social':socialSite.objects.all()
    }
    return render(request, "landing/helpCenter.html", dist)
def thisProduct(request,id):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    product = Product.objects.get(id = id)
    all = Product.objects.filter(hide=False).order_by('ordering')
    allSub = Sub_product.objects.filter(hide=False)
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'product':product,
        'all':all,
        'allSub':allSub,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        contx = {
            'name':name,
            'number':phone,
            'email':email,
            'product':product.name,
            'message':message
        }
      
        email_from = settings.EMAIL_HOST_USER
        try:
            message = get_template('contact.html').render(contx)
            msg = EmailMessage(
                'Subject',
                message,
                email_from,
                [setting.product_email],
            )
            msg.content_subtype ="html"# Main content is now text/html
            msg.send()
            messages.success(request,"Successfully Sent Message")
        except:
            messages.success(request,"Fail Sending Mail")
        # real_msg = "Name: "+name+ " I would like to query on "+ str(product.name) + ". Number: " + str(phone) + ". Email: " +str(email) + " Message: " +message
        # try:
        #     send_mail(name+' queries on '+str(product.name), real_msg, email_from, [setting.product_email] , fail_silently=False,)
        #     messages.success(request,"Successfully Sent Message")
        # except:
        #     messages.success(request,"Fail Sending Mail")
        return HttpResponseRedirect(reverse('landing:thisProduct',args=[product.id]))
    return render(request, "landing/thisproduct.html", dist)


def subProduct(request, id):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    product = Sub_product.objects.get(id = id)
    all = Sub_product.objects.filter(hide=False)
    allPro = Product.objects.filter(hide=False).order_by('ordering')
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'product':product,
        'all':all,
        'allPro':allPro,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        contx = {
            'name':name,
            'number':phone,
            'email':email,
            'product':product.name,
            'message':message
        }
      
        email_from = settings.EMAIL_HOST_USER
        try:
            message = get_template('contact.html').render(contx)
            msg = EmailMessage(
                'Subject',
                message,
                email_from,
                [setting.product_email],
            )
            msg.content_subtype ="html"# Main content is now text/html
            msg.send()
            messages.success(request,"Successfully Sent Message")
        except:
            messages.success(request,"Fail Sending Mail")
        # real_msg = "Name: "+name+ " I would like to query on "+ str(product.name) + ". Number: " + str(phone) + ". Email: " +str(email) + " Message: " +message
        # try:
        #     send_mail(name+' queries on '+str(product.name), real_msg, email_from, [setting.product_email] , fail_silently=False,)
        #     messages.success(request,"Successfully Sent Message")
        # except:
        #     messages.success(request,"Fail Sending Mail")
        return HttpResponseRedirect(reverse('landing:thisProduct',args=[product.id]))
    return render(request, "landing/subproduct.html", dist)

def faq(request):
    PageVisitView()
    sett = Setting.objects.all()
    faq = QuestionAnswer.objects.all().order_by('ordering')
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    for i in faq:
        show = i.id
        break
    dist ={
        'setting':setting,
        'faq':faq,
        'show':show,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    return render(request, "landing/training.html", dist)

def sitemap(request):
    PageVisitView()
    sett = Setting.objects.all()
    setting = None
    product = Product.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist ={
        'setting':setting,
        'product':product,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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

    report = Report.objects.all().order_by('-id')
    Yeara = fiscalYear.objects.all().order_by('-id')
    for i in Yeara:
        bb = i.id
        break

    media = settings.MEDIA_ROOT
    aa = media.replace('\\media',"")
    dist = {
        'rep':report,
        'aa':aa,
        'bb':bb,
        'fis':Yeara,
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
    elif slug=="others":
        rep = OtherDownload.objects.get(id=id)
    else:
        rep = Download.objects.get(id = id)
    # file = open(aa+"/"+rep.files.url, "rb").read()
    file = open(aa+rep.files.url, "rb").read()
    rea_response = HttpResponse(file, content_type='application/pdf')
    rea_response['Content-Disposition'] = 'attachment; filename={}'.format(rep.name+'.pdf')
    return rea_response


def pdf_view(request,slug, id):
    media = settings.MEDIA_ROOT
    # aa = media.replace('\\media',"")
    aa = media.replace('/media/',"")
    if slug == 'report':
        rep = Report.objects.get(id=id)
    elif slug=="news":
        rep = news.objects.get(id=id)
    elif slug=="others":
        rep = OtherDownload.objects.get(id=id)
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


def Thenews(request,id):
    new = news.objects.get(id = id)
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'news':new,
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    return render(request, "landing/news.html", dist)
def surveyor(request):
    PageVisitView()
    s = Surveryor.objects.all().order_by('-id')
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        's':s,
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    return render(request, "landing/surveyor.html", dist)

def agents(request):
    PageVisitView()
    s = Agent.objects.all().order_by('-id')
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        's':s,
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }

    return render(request, "landing/agents.html", dist)

def citizen(request):
    PageVisitView()
    s = Citizen.objects.all().order_by('-id')
    sett = Setting.objects.all()
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        's':s,
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['branch']
        branch = Branch.objects.filter(Q(district__icontains=name) | Q(street__icontains=name)| Q(BranchName__icontains=name))
        if branch:
            found= False
        else:
            found= True
        distS = {
            'branch':branch,
            'Nfound':found,
            'setting':setting,
            'bar':TopBar.objects.all(),
            'social':socialSite.objects.all()
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
  
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
    }
    return render(request, "landing/gallary.html", dist)

def download(request):
    PageVisitView()
    d = news.objects.all().order_by('-dateof')
    sett = Setting.objects.all()
   
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'd':d,
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
    files = Download.objects.all().order_by('-id')
    sett = Setting.objects.all()
    other = OtherDownload.objects.all().order_by('-id')
    setting = None
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'files':files,
        'setting':setting,
        'other':other,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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
        'setting':setting,
        'bar':TopBar.objects.all(),
        'social':socialSite.objects.all()
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

def career(request):
    setting = None
    sett = Setting.objects.all()
    if sett:
        for i in sett:
            setting = i 
            break
    dist = {
        'bar':TopBar.objects.all(),
        'setting':setting,
        'social':socialSite.objects.all()
    }
    return render(request, "landing/carrer.html", dist)

def changedis(request):
    br = Branch.objects.all()
    for i in br:
        i.BranchName = i.district
        i.save()
    return HttpResponse('/')