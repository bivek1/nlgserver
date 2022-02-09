from django.urls import path
from .import views

app_name = "landing"

urlpatterns = [
    path('', views.landing, name = "landing"),
    path('products', views.productPolicy, name = "productPolicies"),
    path('aboutus', views.aboutUs, name = "aboutUs"),
    path('statement', views.finance, name = "finance"),
    path('branches', views.branch, name = "branch"),
    path('surveyor', views.surveyor , name ="surveyor"),
    path('agents', views.agents , name ="agents"),
    path('citizenscharter', views.citizen , name ="citizen"),
    path('gallary', views.gallery, name ="gallary"),
    path('downloadNews', views.download, name="download"),
    path('news/<int:id>', views.Thenews, name="news"),
    path('filedownload/<slug:slug>/<int:id>/', views.filedownload, name="filedownload"),
    path('viewDocument/<slug:slug>/<int:id>', views.pdf_view, name ="pdfview"),
    path('checklogin', views.checkLogin, name = 'checkLogin'),
    path('contactus', views.contact, name = "contact"),
    path('faq', views.faq, name = "faq"),
    path('term', views.term, name = "term"),
    path("training", views.training, name ="training"),
    path('sitemaps', views.sitemap, name ="sitemap"),
    path('downloadfile', views.downloadFile, name="downloadFile"),
    path('productDetails/<int:id>', views.thisProduct, name="thisProduct"),
    path('subproductDetails/<int:id>', views.subProduct, name="subProduct"),
    path('carrer', views.career, name="carrer"),


    # Calculator
    path('premiumcalculator', views.calculator, name="calculator"),
    path('carCalculator', views.carCalculator, name ="carCalculator"),
    path('tempocalculator', views.tempoCal, name ="tempoCal"),
    path('taxicalculator', views.taxiCal, name ="taxiCal"),
    path('goodcalculator', views.goodCal, name ="goodCal"),
    path('agricalculator', views.agriCal, name="agriCal"),
    path('fuelcalculator', views.fuelTank, name ="fuelCal"),
    path('passengercalculator', views.passenger, name = "passengerCal"),
    path('tractorcalculator', views.tractor, name = "tractorcal"),
    path('constructioncalculator', views.con, name = "con"),
    

    path('productCalculator', views.productCal, name ="productCal"),
    path('PropertyCalculator', views.propertyCal, name ="propertyCal"),
    path('PersonalAccidentCalculator', views.personal, name ="personalCal"),
    path('agriculterCalculator', views.agriCal, name = 'agriCal'),
    path('login', views.logIn, name= "login"),

    path('helpCenter', views.helpCen, name="helpCenter"),
    path('changedistrictname', views.changedis),
]
