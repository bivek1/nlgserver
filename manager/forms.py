from django import forms
from landing.models import Branch,Surveryor,Agent,Citizen,Report,news, Setting, Announcement, Sub_product, Product, Bod, ManagementTeam, QuestionAnswer
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class BranchF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BranchF, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
            
    
    class Meta:
        model = Branch
        fields = ('__all__')

        widgets = {
            'district': forms.TextInput(attrs={'placeholder':'Kathmandu'}),
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
       
        
class AgentF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AgentF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    class Meta:
        model = Agent
        fields = ('__all__')
        
class CitizenF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CitizenF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Citizen
        fields = ('__all__')   

class ReportF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ReportF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Report
        fields = ('__all__')   
        exclude= ('slug',)
        
class newsF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(newsF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = news
        fields = ('__all__')   
        exclude = ('slug',)

class BodForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Bod
        fields = ('__all__')   

        widgets =  {
            'name': forms.TextInput(attrs={'placeholder':'Name of the Bod'}),
            'image': forms.FileInput(),
            'post': forms.TextInput(attrs={'placeholder':'Post of Bod'}),
            'type' :forms.TextInput(attrs={'placeholder':'Samuka Ka'}),
            'email' : forms.EmailInput(attrs={'placeholder':'user@nlgi.com'}),
            'appointed_date': forms.DateInput(attrs={'type':'date'}),
           
            're_appointed_date':forms.DateInput(attrs={'type':'date'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone Number'}),
            'descriptipn' : forms.TextInput(attrs={'placeholder':'Short Description'}),
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
            'name': forms.TextInput(attrs={'placeholder':'Name of the Team'}),
            'image': forms.FileInput(),
            'post': forms.TextInput(attrs={'placeholder':'Post of the Team'}),
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
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Name of the Product"}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'description': CKEditorUploadingWidget()
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
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Name of the Product"}),
            'image':forms.FileInput(attrs={'class':'form-control ps-0 form-control-line'}),
            'product': forms.Select(attrs={'class':'form-control ps-0 form-control-line'}),
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
            'question': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Add a Questions"}),
            'answer':forms.Textarea(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Add a Descriptions"}),
           
        }
        
        
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model= Announcement
        fields=('__all__')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control ps-0 form-control-line','placeholder':"Announcement Name"}),
            'image': forms.FileInput(attrs={'class':'form-control ps-0'}),
            'starting_date': forms.DateInput(attrs={'type':'date','class':'form-control ps-0 form-control-line'}),
            'ending_date': forms.DateInput(attrs={'type':'date', 'class':'form-control ps-0 form-control-line'}),
        }