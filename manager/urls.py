from django.urls import path
from .import views
app_name = "manager"

urlpatterns = [
    path('dashboard', views.dashboard, name ="dashboard"),
    path('logout', views.logoutUser, name="logout"),
    path('addAgent', views.addAgent, name='addAgent'),
    path('addBranch', views.addBranch, name='addBranch'),
    path('addSurveryor', views.addSurveryor, name='addSurveryor'),
    path('addCitizen', views.addCitizen, name='addCitizen'),
    path('addNews', views.addNews, name='addNews'),
    path('addReport', views.addReport, name='addReport'),
    path('formReport/<int:id>', views.formReport, name="formReport"),
    path('statementReport/<int:id>', views.statementReport, name="statementReport"),
    path('newUpdate', views.newUpdate, name = "newUpdate"),
    path('settings', views.setting, name="setting"),
    path('deleteBranch/<int:id>', views.deleteBranch, name = "deleteBranch"),
    path('Bod', views.addBod, name ="addBod"),
    path('managementTeam', views.managementTeam, name='managementTeam'),
    path('addproducts', views.ProductView, name="product"),
    path('subproduct', views.SubProductView, name="subProduct"),
    path('questionAnswer', views.QuestionAnswerView, name="questionAnswer"),
    path('announcement', views.AnnouncementView, name="announcement")
 
]

