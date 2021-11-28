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
 
]

