from django.db import models
from django.db.models.fields import CharField, SlugField, related
from django.urls import reverse



class Branch(models.Model):
    district = models.CharField(max_length=70, null = True, blank= True)
    provience = models.CharField(max_length=20, choices=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    ), null= True, blank= True)
    street = models.CharField(max_length=50, null = True, blank= True)
    contact = models.CharField(max_length=50, null = True, blank= True)
    fax = models.CharField(max_length=50, null = True, blank= True)
    email = models.CharField(max_length=50, null = True, blank= True)
    focal = models.CharField(max_length=50, null = True, blank= True)
    number = models.CharField(max_length=50, null = True, blank= True)
    focal_img = models.ImageField(upload_to ="focalperson", default="/downlogo.PNG")



class Surveryor(models.Model):
    name = models.CharField(max_length=200, null = True, blank= True)
    specilization = models.CharField(max_length=100, null = True, blank= True)
    area = models.CharField(max_length=100, null = True, blank= True)
    contact = models.CharField(max_length=100, null = True, blank= True)
    email = models.CharField(max_length=100, null = True, blank= True)
   
    
    def __str__(self):
        return self.name
    
    
class Agent(models.Model):
    name = models.CharField(max_length=500, null = True, blank= True)
    address = models.CharField(max_length=100, null = True, blank= True)
    contact = models.CharField(max_length=100, null = True, blank= True)
    email = models.CharField(max_length=100, null = True, blank= True)
   
    
    def __str__(self):
        return self.name
    
class Citizen(models.Model):
    name = models.CharField(max_length=500, null = True, blank= True)
    details = models.CharField(max_length=1000, null = True, blank= True)
    
    
class fiscalYear(models.Model):
    fiscal = models.CharField(max_length=200)

    def __str__(self):
        return self.fiscal

class Report(models.Model):
    name = models.CharField(max_length = 200)
    fiscal = models.ForeignKey(fiscalYear, null= True, related_name='fiscalyear', blank= True, on_delete=models.PROTECT)
    slug = models.SlugField(default='report')
    rtype = models.CharField(max_length = 200, choices = (
        ('Annual Report', 'Annual Report'),
        ('Quarterly Report', 'Quarterly Report'),
        ('Minute Report', 'Minute Report'),
        ('Other Report', 'Other Report'),
    ))
    files = models.FileField(upload_to='Report/')
    
    def __str__(self):
        return self.name
    
    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])


    
class news(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=2000, null= True, blank= True)
    slug = models.SlugField(default='news')
    dateof = models.DateField(auto_now_add=True, null= True, blank= True) 
    files = models.FileField(upload_to='News/',  null= True, blank= True)
    image = models.ImageField(upload_to="images/", null= True, blank= True)
    
    def __str__(self):
        return self.name

    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])


class Download(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(default='download')
    dtype = models.CharField(max_length = 200, choices = (
        ('KYC Form', 'KYC Form'),
        ('Proposal Form', 'Proposal Form'),
        ('Claim Form', 'Claim Form'),
    ))
    files = models.FileField(upload_to='Report/')
    
    def __str__(self):
        return self.name

    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])
    

    
