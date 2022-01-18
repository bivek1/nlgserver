from django import forms
from django.forms import fields, widgets
from landing.models import fiscalYear, Branch, Download,Surveryor,Agent,Citizen,Report,news, Setting, Announcement, Sub_product, Product, Bod, ManagementTeam, QuestionAnswer, DepartmentHead

class FiscalForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FiscalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    class Meta:
        model= fiscalYear
        fields = ('__all__')

        widgets = {
            'fiscal': forms.TextInput(attrs={'placeholder':'write in this format 2078/2079', 'required':True}),

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
            'district': forms.TextInput(attrs={'placeholder':'Kathmandu', 'required':True}),
            'provience': forms.Select(attrs={'placeholder':'1', 'required':True}),
            'street': forms.TextInput(attrs={'placeholder':'Lazimpat, Kathmandu Nepal', 'required':True}),
            'contact': forms.TextInput(attrs={'placeholder':'01442541', 'required':True}),
            'fax': forms.TextInput(attrs={'placeholder':'010101210'}),
            'email': forms.TextInput(attrs={'placeholder':'info@nlgi.com', 'required':True}),
            'focal': forms.TextInput(attrs={'placeholder':'Person Name', 'required':True}),
            'number': forms.TextInput(attrs={'placeholder':'Focal Number', 'required':True}),
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
            'name':forms.TextInput(attrs={'placeholder':'Name of the Surveryor', 'required':True}),
            'specilization':forms.TextInput(attrs={'placeholder':'Specilization of the Surveryor', 'required':True}),
            'lience_no':forms.TextInput(attrs={'placeholder':'Licence No. of the Surveryor', 'required':True}),
            'issued_date':forms.DateInput(attrs={'type':'date'}),
            'renew_date':forms.DateInput(attrs={'type':'date'}),
            'area':forms.TextInput(attrs={'placeholder':'Area', 'required':True}),
            'contact':forms.TextInput(attrs={'placeholder':'Contact No. of the Surveryor', 'required':True}),
            'email':forms.EmailInput(attrs={'placeholder':'surveryor@nlgi.com', 'required':True}),
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
            'name':forms.TextInput(attrs={'placeholder':'Name of the Agents', 'required':True}),
            'address':forms.TextInput(attrs={'placeholder':'Address of the Agent', 'required':True}),
            'contact':forms.TextInput(attrs={'placeholder':'Contact of the Agents', 'required':True}),
            'email':forms.TextInput(attrs={'placeholder':'Email@email.com', 'required':True}),
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
            'name':forms.TextInput(attrs={'placeholder':'Name of the Citizen', 'required':True}),
            'details':forms.TextInput(attrs={'placeholder':'Details of the Citizen', 'required':True}),
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
            'name':forms.TextInput(attrs={'placeholder':'Name of the Report', 'required':True})
        }
        
class newsF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(newsF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = news
        fields = ('__all__')   
        exclude = ('slug',)
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name of the News', 'required':True}),
            'description':forms.TextInput(attrs={'placeholder':'Description of the News', 'required':True})
        }

class BodForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BodForm, self).__init__(*args, **kwargs)

    
    class Meta:
        model = Bod
        fields = ('__all__')   

        widgets =  {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Name of the Bod', 'required':True}),
            'image': forms.FileInput(),
            'post': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Post of Bod', 'required':True}),
            'type' :forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Samuka Ka'}),
            'email' : forms.EmailInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'user@nlgi.com'}),
            'appointed_date': forms.DateInput(attrs={'class':'form-control ps-0 form-control-line','type':'date'}),
            'chairman':forms.CheckboxInput(),
            're_appointed_date':forms.DateInput(attrs={'class':'form-control ps-0 form-control-line','type':'date'}),
            'phone': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Phone Number'}),
            'descriptipn' : forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Short Description'}),
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
            'name': forms.TextInput(attrs={'placeholder':'Name of the Team', 'required':True}),
            'image': forms.FileInput(),
            'post': forms.TextInput(attrs={'placeholder':'Post of the Team', 'required':True}),
            'email' : forms.EmailInput(attrs={'placeholder':'user@nlgi.com'}),
            'appointed_date': forms.DateInput(attrs={'type':'date'}),
            're_appointed_date':forms.DateInput(attrs={'type':'date'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone Number'}),
        }

class ProductFrom(forms.ModelForm):
     
    class Meta:
        model = Product
        fields = ('__all__')    

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Name of the Product", 'required':True}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'description': forms.Textarea(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Add a Description', 'required':True}),
            'icons': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"fa fa-motorcycle"}),
        }   

class SubProductFrom(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SubProductFrom, self).__init__(*args, **kwargs)
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Sub_product
        fields = ('__all__') 

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Name of the Product", 'required':True}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'product': forms.Select(attrs={'class':'form-control ps-0 form-control-line', 'required':True}),
            'description': forms.Textarea(attrs={'class':'form-control ps-0 form-control-line','placeholder':'Add a Description', 'required':True}),
            'discontinue': forms.CheckboxInput()
        }

class QuestionAnswerFrom(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(QuestionAnswerFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = QuestionAnswer
        fields = ('__all__') 

        widgets = {
            'question': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Add a Questions", 'required':True}),
            'answer':forms.Textarea(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Add a Descriptions", 'required':True}),
           
        }
        
        
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model= Announcement
        fields=('__all__')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Announcement Name", 'required':True}),
            'image': forms.FileInput(attrs={'class':'form-control ps-0', 'required':True}),
            'starting_date': forms.DateInput(attrs={'type':'date','class':'form-control ps-0 form-control-line', 'required':True}),
            'ending_date': forms.DateInput(attrs={'type':'date', 'class':'form-control ps-0 form-control-line', 'required':True}),
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