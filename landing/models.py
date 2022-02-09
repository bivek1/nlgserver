from statistics import mode
from ckeditor.fields import RichTextField 
from django.db import models
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from ckeditor_uploader.fields import RichTextUploadingField


district = (
    ('Taplejung','Taplejung'),
    ('Panchthar','Panchthar'),
    ('Ilam','Ilam'),
    ('Jhapa','Jhapa'),
    ('Sankhuwasabha','Sankhuwasabha'),
    ('Bhojpur','Bhojpur'),
    ('Terhathum','Terhathum'),
    ('Dhankuta','Dhankuta'),
    ('Morang','Morang'),
    ('Sunsari','Sunsari'),
    ('Solukhumbu','Solukhumbu'),
    ('Okhaldhunga','Okhaldhunga'),
    ('Khotang','Khotang'),
    ('Udayapur','Udayapur'),
    ('Siraha','Siraha'),
    ('Saptari','Saptari'),
    ('Dolakha','Dolakha'),
    ('Ramechhap','Ramechhap'),
    ('Sindhuli','Sindhuli'),
    ('Sarlahi','Sarlahi'),
    ('Mahottari','Mahottari'),
    ('Dhanusha','Dhanusha'),
    ('Sindhupalchowk','Sindhupalchowk'),
    ('Rasuwa','Rasuwa'),
    ('Kavrepalanchowk','Kavrepalanchowk'),
    ('Dhading','Dhading'),
    ('Kathmandu','Kathmandu'),
    ('Lalitpur','Lalitpur'),
    ('Bhaktapur','Bhaktapur'),
    ('Nuwakot','Nuwakot'),
    ('Parsa','Parsa'),
    ('Bara','Bara'),
    ('Makwanpur','Makwanpur'),
    ('Chitwan','Chitwan'),
    ('Rautahat','Rautahat'),
    ('Gorkha','Gorkha'),
    ('Lamjung','Lamjung'),
    ('Tanahun','Tanahun'),
    ('Kaski','Kaski'),
    ('Syangja','Syangja'),
    ('Manang','Manang'),
    ('Nawalpur','Nawalpur'),
    ('Gulmi','Gulmi'),
    ('Kapilbastu','Kapilbastu'),
    ('Palpa','Palpa'),
    ('Rupandehi','Rupandehi'),
    ('Arghakhachi','Arghakhachi'),
    ('Mustang','Mustang'),
    ('Parbat','Parbat'),
    ('Myagdi','Myagdi'),
    ('Baglung','Baglung'),
    ('Eastern Rukum','Eastern Rukum'),
    ('Salyan','Salyan'),
    ('Rolpa','Rolpa'),
    ('Pyuthan','Pyuthan'),
    ('Dang','Dang'),
    ('Dolpa','Dolpa'),
    ('Humla','Humla'),
    ('Mugu','Mugu'),
    ('Jumla','Jumla'),
    ('Kalikot','Kalikot'),
    ('Jajarkot','Jajarkot'),
    ('Banke','Banke'),
    ('Dhailekh','Dhailekh'),
    ('Surkhet','Surkhet'),
    ('Bardiya','Bardiya'),
    ('Achham','Achham'),
    ('Bajhang','Bajhang'),
    ('Kailali','Kailali'),
    ('Doti','Doti'),
    ('Bajura','Bajura'),
    ('Kanchanpur','Kanchanpur'),
    ('Baitadi','Baitadi'),
    ('Dadeldhura','Dadeldhura'),
    ('Darchula','Darchula'),
    ('Western Rukum','Western Rukum'),
    ('Parasi','Parasi')
)


class Branch(models.Model):
    BranchName = models.CharField(max_length=100, null = True, blank= True)
    district = models.CharField(max_length=70, choices=district, null = True, blank= True)
    provience = models.CharField(max_length=20, choices=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
    ), null= True, blank= True)
    street = models.CharField(max_length=50, null = True, blank= True)
    contact = models.CharField(max_length=50, null = True, blank= True)
    fax = models.CharField(max_length=50, null = True, blank= True)
    email = models.CharField(max_length=50, null = True, blank= True)
    focal = models.CharField(max_length=50, null = True, blank= True)
    number = models.CharField(max_length=50, null = True, blank= True)
    focal_img = models.ImageField(upload_to ="focalperson", default="/downlogo.PNG")
    objects = models.Manager()

    def __str__(self):
        return self.BranchName
    def clear(self):
        return reverse('manager:deleteImage',args=[self.id, 'branch'])

class Surveryor(models.Model):
    name = models.CharField(max_length=200, null = True, blank= True, )
    specilization = models.CharField(max_length=100, null = True, blank= True, )
    lience_no = models.CharField(max_length=100, null = True, blank = True, )
    issued_date = models.DateField(null = True, blank = True)
    renew_date = models.DateField(null = True, blank=True)
    area = models.CharField(max_length=100, null = True, blank= True, )
    contact = models.CharField(max_length=100, null = True, blank= True, )
    email = models.CharField(max_length=100, null = True, blank= True, )
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
    
class Agent(models.Model):
    name = models.CharField(max_length=500, null = True, blank= True, )
    address = models.CharField(max_length=100, null = True, blank= True, )
    contact = models.CharField(max_length=100, null = True, blank= True)
    lience_no = models.CharField(max_length=100, null = True, blank= True)
    issue_date = models.DateField(null = True, blank= True, )
    email = models.CharField(max_length=100, null = True, blank= True, )
    agent_code = models.CharField(max_length=200, null = True, blank= True, )
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
class Citizen(models.Model):
    name = models.CharField(max_length=500, null = True, blank= True, )
    details = RichTextUploadingField(null = True, blank= True, )
    objects = models.Manager()

    def __str__(self):
        return self.name
    
class fiscalYear(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    fiscal = models.CharField(max_length=200)
    objects = models.Manager()
    def __str__(self):
        return self.fiscal
   
class Report(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    slug = models.SlugField(default='report')
    fiscal = models.ForeignKey(fiscalYear, null= True, related_name='fiscalyear', blank= True, on_delete=models.PROTECT)
    rtype = models.CharField(max_length = 200, choices = (
        ('Annual Report', 'Annual Report'),
        ('Quarterly Report', 'Quarterly Report'),
        ('Minute Report', 'Minute Report'),
        ('Other Report', 'Other Report'),
    ))
    files = models.FileField(upload_to='Report/', null = True, blank = True)
    objects = models.Manager()
    def __str__(self):
        return self.name

    def clearfiles(self):
        return reverse('manager:deleteReport',args=[self.id, 'report'])
    
    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])

class news(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(default='news')
    description = RichTextUploadingField(null = True, blank = True)
    dateof = models.DateField(auto_now_add=False, null= True, blank= True) 
    files = models.FileField(upload_to='News/',  null= True, blank= True)
    image = models.ImageField(upload_to="images/", null= True, blank= True)
    objects = models.Manager()
    def __str__(self):
        return self.name

    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])

    def clearfiles(self):
        return reverse('manager:deleteReport',args=[self.id, 'news'])

    def clear(self):
        return reverse('manager:deleteImage',args=[self.id, 'news'])
       
class Download(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    slug = models.SlugField(default='download')
    dtype = models.CharField(max_length = 200, choices = (
        ('KYC Form', 'KYC Form'),
        ('Proposal Form', 'Proposal Form'),
        ('Claim Form', 'Claim Form'),
    ))
    files = models.FileField(upload_to='Report/', null = True, blank = True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])

    def clearfiles(self):
        return reverse('manager:deleteReport',args=[self.id, 'form'])
    
class Bod(models.Model):
    ordering = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "management/", null = True, blank= True)
    post = models.CharField(max_length=200,null = True, blank= True , )
    type = models.CharField(max_length=100, null = True, blank= True, )
    email = models.EmailField(null = True, blank= True, )
    appointed_date = models.DateField(null = True, blank= True)
    re_appointed_date = models.DateField(null = True, blank=True)
    phone = models.CharField(max_length=100,null = True, blank = True, )
    description = RichTextUploadingField(null = True, blank = True, )
    chairman = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.name
    
    def clear(self):
        return reverse('manager:deleteImage',args=[self.id, 'bod'])

class ManagementTeam(models.Model):
    ordering = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "management/", null = True, blank= True)
    post = models.CharField(max_length=200, null = True, blank= True , )
    email = models.EmailField(null = True, blank=True, )
    appointed_date = models.DateField(null = True, blank=True)
    re_appointed_date = models.DateField(null = True, blank=True)
    phone = models.CharField(max_length=200,null = True, blank = True)
    objects = models.Manager()

    def __str__(self):
        return self.name
    
    def clear(self):
        return reverse('manager:deleteImage',args=[self.id, 'management'])

class Product(models.Model):
    ordering = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "products/", null = True, blank=True)
    description = RichTextUploadingField(null = True, blank = True)
    icons = models.CharField(max_length=20, null = True, blank=True)
    
    discontinue = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
    objects = models.Manager()
    def __str__(self):
        return self.name
    
   

class Sub_product(models.Model):
    product = models.ForeignKey(Product, related_name="sub_product", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "products/",null = True, blank = True)
    description = RichTextUploadingField(null = True, blank = True)
    discontinue = models.BooleanField(default=False)
    icons = models.CharField(max_length=20, null = True, blank=True)
    hide = models.BooleanField(default=False)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

class QuestionAnswer(models.Model):
    ordering = models.IntegerField()
    question = models.CharField(max_length=500)
    answer = RichTextUploadingField(null = True, blank = True)
    objects = models.Manager()

    def __str__(self):
        return self.question

class CeoMessage(models.Model):
    message = RichTextUploadingField()

    objects = models.Manager()

    def __str__(self):
        return self.message

class Setting(models.Model):
    logo = models.ImageField(upload_to ="logo/", null=True, blank=True)
    email = models.EmailField(default="info@nlgi.com.np")
    product_email = models.EmailField(default="underwriting@nlgi.com.np")
    number1 = models.CharField(max_length = 12, default="01-4442646")
    number2 = models.CharField(max_length = 12, default="01-4006648", null = True, blank=True)
    toll_free_no = models.BigIntegerField(default="16600199099", null = True, blank=True)
    location = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return f"{self.email} -  {self.number1}"


class Announcement(models.Model):
    name = models.CharField(max_length=200,null = True, blank = True)
    image = models.ImageField(upload_to ="announcement",null = True, blank = True)
    description = RichTextUploadingField(null = True, blank = True)
    link = models.CharField(max_length = 300, null = True, blank = True)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

class DepartmentHead(models.Model):
    ordering = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "departmenthead/",null = True, blank = True)
    post = models.CharField(max_length=100,null = True, blank = True)
    email = models.EmailField(max_length=100,null = True, blank = True)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

    def clear(self):
        return reverse('manager:deleteImage',args=[self.id, 'department'])

class PageVisit(models.Model):
    count = models.BigIntegerField()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.count

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null = True)
    phone = models.BigIntegerField(blank=True, null = True)
    subject = models.CharField(max_length=200,null = True, blank = True)
    message = models.CharField(max_length=1000,null = True, blank = True)
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

class OtherDownload(models.Model):
    name = models.CharField(max_length=200, null = True, blank = True)
    slug = models.SlugField(default='others')
    files = models.FileField(upload_to='other/', null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def download(self):
        return reverse('landing:filedownload', args=[self.slug, self.id])

    def pdf(self):
        return reverse('landing:pdfview', args=[self.slug, self.id])


class socialSite(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    icon = models.CharField(max_length=20, null=True, blank= True)
    link = models.CharField(max_length=1000, null=True, blank= True)
    objects = models.Manager()

   
    def __str__(self):
        return self.name

class helpCenter(models.Model):
    title = models.CharField(max_length=200, null = True, blank = True)
    description = RichTextUploadingField(null = True, blank = True)

    objects = models.Manager()

   
    def __str__(self):
        return self.title


class TopBar(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    hide = models.BooleanField(default=False)
    link = models.CharField(max_length=200, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class RIpartner(models.Model):
    description = RichTextUploadingField()

    def __str__(self):
        return f"{self.description}"


