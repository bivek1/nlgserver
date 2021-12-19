from django.db import models
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
    objects = models.Manager()


class Surveryor(models.Model):
    name = models.CharField(max_length=200, null = True, blank= True)
    specilization = models.CharField(max_length=100, null = True, blank= True)
    lience_no = models.BigIntegerField(null = True, blank = True)
    issued_date = models.DateField(null = True, blank = True)
    renew_date = models.DateField(null = True, blank=True)
    area = models.CharField(max_length=100, null = True, blank= True)
    contact = models.CharField(max_length=100, null = True, blank= True)
    email = models.CharField(max_length=100, null = True, blank= True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
    
class Agent(models.Model):
    name = models.CharField(max_length=500, null = True, blank= True)
    address = models.CharField(max_length=100, null = True, blank= True)
    contact = models.CharField(max_length=100, null = True, blank= True)
    email = models.CharField(max_length=100, null = True, blank= True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
class Citizen(models.Model):
    name = models.CharField(max_length=500, null = True, blank= True)
    details = models.CharField(max_length=1000, null = True, blank= True)
    objects = models.Manager()
    
class fiscalYear(models.Model):
    fiscal = models.CharField(max_length=200)
    objects = models.Manager()
    def __str__(self):
        return self.fiscal

class Report(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(default='report')
    fiscal = models.ForeignKey(fiscalYear, null= True, related_name='fiscalyear', blank= True, on_delete=models.PROTECT)
    rtype = models.CharField(max_length = 200, choices = (
        ('Annual Report', 'Annual Report'),
        ('Quarterly Report', 'Quarterly Report'),
        ('Minute Report', 'Minute Report'),
        ('Other Report', 'Other Report'),
    ))
    files = models.FileField(upload_to='Report/')
    objects = models.Manager()
    def __str__(self):
        return self.name
    
    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])


    
class news(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(default='news')
    description = models.CharField(max_length=2000, null= True, blank= True)
    dateof = models.DateField(auto_now_add=True, null= True, blank= True) 
    files = models.FileField(upload_to='News/',  null= True, blank= True)
    image = models.ImageField(upload_to="images/", null= True, blank= True)
    objects = models.Manager()
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
    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])
    
class Bod(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "management/")
    post = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    email = models.EmailField()
    appointed_date = models.DateField()
    re_appointed_date = models.DateField(null = True, blank=True)
    phone = models.BigIntegerField(null = True, blank = True)
    descriptipn = models.CharField(max_length=1000)
    chairman = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.name

class ManagementTeam(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "management/")
    post = models.CharField(max_length=200)
    email = models.EmailField(null = True, blank=True)
    appointed_date = models.DateField(null = True, blank=True)
    re_appointed_date = models.DateField(null = True, blank=True)
    phone = models.BigIntegerField(null = True, blank = True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "products/")
    description = models.CharField(max_length=2000)
    icons = models.CharField(max_length=20, null = True, blank=True)
    objects = models.Manager
    discontinue = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Sub_product(models.Model):
    product = models.ForeignKey(Product, related_name="sub_product", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "products/")
    description = models.CharField(max_length=2000)
    discontinue = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
    objects = models.Manager
    
    def __str__(self):
        return self.name

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)
    objects = models.Manager()

    def __str__(self):
        return self.question

class Setting(models.Model):
    logo = models.ImageField(upload_to ="logo/", null=True, blank=True)
    email = models.EmailField(default="info@nlgi.com.np")
    number1 = models.BigIntegerField(default="01-4442646")
    number2 = models.BigIntegerField(default="01-4006648", null = True, blank=True)
    toll_free_no = models.BigIntegerField(default="16600199099", null = True, blank=True)
    location = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return f"{self.email} -  {self.number1}"


class Announcement(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ="announcement")
    starting_date = models.DateField()
    ending_date = models.DateField()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

class DepartmentHead(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "departmenthead/")
    post = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

class PageVisit(models.Model):
    count = models.BigIntegerField()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.count

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null = True)
    phone = models.BigIntegerField(blank=True, null = True)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name



    
    
