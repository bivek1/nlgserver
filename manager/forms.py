from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from landing.models import OtherDownload, RIpartner ,helpCenter, socialSite,fiscalYear,CeoMessage, Branch, Download,Surveryor,Agent,Citizen,Report,news, Setting, Announcement, Sub_product, Product, Bod, ManagementTeam, QuestionAnswer, DepartmentHead
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CeoMessageForm(forms.ModelForm):
    class Meta:
        model = CeoMessage
        fields = ('__all__')
    
class RIForm(forms.ModelForm):
    class Meta:
        model = RIpartner
        fields = ('__all__')

class AdminForm(forms.Form):
    email = forms.EmailField(label = 'Email', max_length = 200, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'}))
   
    
    fields = ('email', 'password1','password2')
  
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email
        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
   
    def clean_password1(self):
        data = self.cleaned_data['password1']
        d = str(data)
        if len(d) < 6:
            raise forms.ValidationError("Password must be greater than 6 digits")
        return data
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password Did not Match')
        return password2

class helpForm(forms.ModelForm):
    class Meta:
        model = helpCenter
        fields = ('__all__')
        widgets =  {
            'title':forms.TextInput(attrs={'class':'form-control form-control-line', 'placeholder':'Title'}),
            'description':CKEditorUploadingWidget(),
          
        }

class socialSiteForm(forms.ModelForm):
    class Meta:
        model = socialSite
        fields = ('__all__')
        widgets =  {
            'name':forms.TextInput(attrs={'class':'form-control form-control-line', 'placeholder':'name of the site'}),
            'icon':forms.TextInput(attrs={'class':'form-control form-control-line', 'placeholder':'fa fa-facebook/youtube/twitter'}),
            'link':forms.TextInput(attrs={'class':'form-control form-control-line', 'placeholder':'Link of your social Site'}),
        }

class OtherDownloadForm(forms.ModelForm):
    class Meta:
        model = OtherDownload
        fields = ('__all__')

        exclude = ('slug',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-line','placeholder':'File Title'}),
            'files':forms.FileInput(attrs={'class':'form-control form-control-line'})
        }

class FiscalForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FiscalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    class Meta:
        model= fiscalYear
        fields = ('__all__')

        widgets = {
            'fiscal': forms.TextInput(attrs={'placeholder':'write in this format 2078/2079'}),

        }
    
class BranchF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BranchF, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
            
    
    class Meta:
        model = Branch
        fields = ('__all__')

        widgets = {
            'BranchName':forms.TextInput(attrs={'placeholder':'Branch Name'}),
            'district': forms.Select(attrs={'placeholder':'Kathmandu'}),
            'provience': forms.Select(attrs={'placeholder':'1'}),
            'street': forms.TextInput(attrs={'placeholder':'Lazimpat, Kathmandu Nepal'}),
            'contact': forms.TextInput(attrs={'placeholder':'01442541'}),
            'fax': forms.TextInput(attrs={'placeholder':'010101210'}),
            'email': forms.TextInput(attrs={'placeholder':'info@nlgi.com'}),
            'focal': forms.TextInput(attrs={'placeholder':'Person Name'}),
            'number': forms.TextInput(attrs={'placeholder':'Focal Number'}),
        }

class SettingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Setting
        fields = ('__all__')
    
class SurveryorF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SurveryorF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Surveryor
        fields = ('__all__')   

        widgets ={
            'name':forms.TextInput(attrs={'placeholder':'Name of the Surveryor'}),
            'specilization':forms.TextInput(attrs={'placeholder':'Specilization of the Surveryor'}),
            'lience_no':forms.TextInput(attrs={'placeholder':'Licence No. of the Surveryor'}),
            'issued_date':forms.DateInput(attrs={'type':'date'}),
            'renew_date':forms.DateInput(attrs={'type':'date'}),
            'area':forms.TextInput(attrs={'placeholder':'Area'}),
            'contact':forms.TextInput(attrs={'placeholder':'Contact No. of the Surveryor'}),
            'email':forms.EmailInput(attrs={'placeholder':'surveryor@nlgi.com'}),
        } 
       
class AgentF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AgentF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    class Meta:
        model = Agent
        fields = ('__all__')

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name of the Agents'}),
            'address':forms.TextInput(attrs={'placeholder':'Address of the Agent'}),
            'contact':forms.TextInput(attrs={'placeholder':'Contact of the Agents'}),
            'email':forms.TextInput(attrs={'placeholder':'Email@email.com'}),
            'lience_no':forms.TextInput(attrs={'placeholder':'Lience Number'}),
            'agent_code':forms.TextInput(attrs={'placeholder':'Agent Code'}),
            'issue_date':forms.TextInput(attrs={'type':'date','placeholder':'Issue Date'}),
        }
        
class CitizenF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CitizenF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Citizen
        fields = ('__all__')   

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Name of the Citizen'}),
            'details':CKEditorUploadingWidget()
        }

class ReportF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ReportF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Report
        fields = ('__all__')   
        exclude= ('slug',)
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name of the Report'})
        }
        
class newsF(forms.ModelForm):
    
   
    class Meta:
        model = news
        fields = ('__all__')   
        exclude = ('slug',)

        labels = {
            'dateof':'Date'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Name of the News'}),
            'dateof':forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','type':'date'}),
            'description':CKEditorUploadingWidget()
        }

class BodForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BodForm, self).__init__(*args, **kwargs)

    
    class Meta:
        model = Bod
        fields = ('__all__')   

        widgets =  {
            'ordering':forms.NumberInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Name of the Bod'}),
            'image': forms.FileInput(),
            'post': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Post of Bod'}),
            'type' :forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Samuka Ka'}),
            'email' : forms.EmailInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'user@nlgi.com'}),
            'appointed_date': forms.DateInput(attrs={'class':'form-control ps-0 form-control-line','type':'date'}),
            'chairman':forms.CheckboxInput(),
            're_appointed_date':forms.DateInput(attrs={'class':'form-control ps-0 form-control-line','type':'date'}),
            'phone': forms.NumberInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Phone Number'}),
            'description' : CKEditorUploadingWidget()
        }

class ManagementForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ManagementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = ManagementTeam
        fields = ('__all__')  

        widgets =  {
            'ordering':forms.NumberInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'name': forms.TextInput(attrs={'placeholder':'Name of the Team'}),
            'image': forms.FileInput(),
            'post': forms.TextInput(attrs={'placeholder':'Post of the Team'}),
            'email' : forms.EmailInput(attrs={'placeholder':'user@nlgi.com'}),
            'appointed_date': forms.DateInput(attrs={'type':'date'}),
            're_appointed_date':forms.DateInput(attrs={'type':'date'}),
            'phone': forms.NumberInput(attrs={'placeholder':'Phone Number'}),
        }

class ProductFrom(forms.ModelForm):
     
    class Meta:
        model = Product
        fields = ('__all__')    

        widgets = {
            'ordering':forms.NumberInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Name of the Product"}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'description': CKEditorUploadingWidget(),
            'icons': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"fa fa-motorcycle"}),
        }   

class SubProductFrom(forms.ModelForm):
    

    class Meta:
        model = Sub_product
        fields = ('__all__') 

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Name of the Product"}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'product': forms.Select(attrs={'class':'form-control ps-0 form-control-line'}),
            'description': CKEditorUploadingWidget(),
            'discontinue': forms.CheckboxInput(),
            'icons': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"fa fa-motorcycle"}),
        }

class QuestionAnswerFrom(forms.ModelForm):
    

    class Meta:
        model = QuestionAnswer
        fields = ('__all__') 

        widgets = {
            'ordering':forms.NumberInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'question': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Add a Questions"}),
            'answer':CKEditorUploadingWidget(),
           
        }
        
        
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model= Announcement
        fields=('__all__')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Announcement Name"}),
            'image': forms.FileInput(attrs={'class':'form-control ps-0'}),
            'link': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line', 'placeholder':'Enter Redirect Link' }),
            'description': CKEditorUploadingWidget(),
        }

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Download
        fields= ('__all__')
        exclude = ('slug',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Name of the Forms'}),
            'dtype': forms.Select(attrs={'class':'form-control ps-0 form-control-line'}),
            'files':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'})
        }
        labels = {
            'dtype':'Form Type'
        }

class DepartmentHeadForm(forms.ModelForm):
    class Meta:
        model = DepartmentHead
        fields = ('__all__')
        widgets = {
            'ordering':forms.NumberInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'name':forms.TextInput(attrs={'class':'form-control ps-0 form-control-line', 'placeholder':'Name of the Department Team'}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'post':forms.TextInput(attrs={'class':'form-control ps-0 form-control-line', 'placeholder':'Post of the Team'}),
            'email':forms.TextInput(attrs={'class':'form-control ps-0 form-control-line', 'placeholder':'Email@nlgi.com'}),
        }

from django.contrib.auth.forms import PasswordChangeForm

class FormChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(FormChangePassword, self).__init__(*args, **kwargs)
        for field in ('old_password', 'new_password1', 'new_password2'):
            self.fields['old_password'].widget.attrs = {'class':'form-control ps-0 form-control-line', 'placeholder':"Old Password"}
            self.fields['new_password1'].widget.attrs = {'class':'form-control ps-0 form-control-line', 'placeholder':"New Password"}
            self.fields['new_password2'].widget.attrs = {'class':'form-control ps-0 form-control-line', 'placeholder':"Re New Password"}