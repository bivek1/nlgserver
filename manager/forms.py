from django import forms
from landing.models import Branch,Surveryor,Agent,Citizen,Report,news



class BranchF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BranchF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = Branch
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
        
class newsF(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(newsF, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control ps-0 form-control-line'
    
    class Meta:
        model = news
        fields = ('__all__')   
        