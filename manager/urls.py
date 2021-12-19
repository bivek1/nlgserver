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
    path('announcement', views.AnnouncementView, name="announcement"),
    path('addForms', views.addForm, name="addForm"),
    path('departmentTeam', views.DepartmentView, name = "departmentTeam"),
    path('deleteAnn/<int:id>', views.deleteAnn, name="deleteAnn"),
    path('deleteProduct/<int:id>', views.deleteProduct, name ="deleteProduct"),
    path('deleteSubProduct/<int:id>', views.deleteSubProduct, name = "deleteSubProduct"),
    path('deleteQuestion/<int:id>', views.deleteQuestion, name = "deleteQuestion"),
    path('deleteDepartment/<int:id>', views.deleteDepartment, name="deleteDepartment"),
    path('deleteAgent/<int:id>', views.deleteAgent, name="deleteAgent"),
    path('deleteCitizen/<int:id>', views.deleteCitizen, name="deleteCitizen"),
    path('deleteSuveryor/<int:id>', views.deleteSuveryor, name="deleteSuveryor"),
    path('deleteBod/<int:id>', views.deleteBod, name="deleteBod"),
    path('deleteManagement/<int:id>', views.deleteManagement, name="deleteManagement"),
    path('deleteReport/<int:id>/<int:type>', views.deleteReport, name="deleteReport"),
    path('deleteForm/<int:id>/<int:type>', views.deleteForm, name="deleteForm"),
    path('deleteNews/<int:id>', views.deleteNews, name="deleteNews"),
    path('editProduct/<int:id>', views.editProduct, name = "editProduct"),
    path('editSubProduct/<int:id>', views.editSubProduct, name = "editSubProduct"),
    path('editQuestionAnswer/<int:id>', views.editQuestion, name = "editQuestionAns"),
    path('editDepartmentteam/<int:id>', views.editDepartment, name ="editDepartment"),
    path('editBranch/<int:id>', views.editBranch, name ="editBranch"),
    path('editAgent/<int:id>', views.editAgent, name ="editAgent"),
    path('editCitizen/<int:id>', views.editCitizen, name ="editCitizen"),
    path('editSurveryor/<int:id>', views.editSurvey, name ="editSurvey"),
    path('editBod/<int:id>', views.editBod, name ="editBod"),
    path('editManagement/<int:id>', views.editManagement, name="editManagement"),
    path('changePassword', views.changePassword, name = "changePassword"),
    path('hideProduct/<int:id>', views.hideProduct, name="hideProduct"),
    path('hideSubProduct/<int:id>', views.hideSubProduct, name="hideSubProduct"),
    path('messages', views.contact, name="contact")
]

