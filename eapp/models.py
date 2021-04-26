from django.db import models

# Create your models here.

ID_CHOICES=[('aadhar','Aadhar Card'),
            ('vid','Voter ID Card'),
            ('passport','Passport'),
            ('dl','Driving Licence')
]
COMPANY_CHOICES=[('pvt.','Pvt. Ltd.'),('limited','Limited'),
                ('ltd.','Ltd.'),
                ('proprietor','Proprietor')
]
LOCATION_CHOICES=[('national','National'), ('international','International'), ('domestic','Domestic'), ('village','Village')
]
AREA_CHOICES=[('it','IT'), ('sales & marketing','Sales & marketing'), ('accounting','Accounting'),
              ('data entry','Data Entry')
]
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,55)]
WORK_CHOICES=[('developer','Developer'), ('designer','Designer'), ('accountant','Accountant'),
              ('sales & management','Sales & Management'), ('e-commerce','E-commerce')
]
# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta():
        db_table="Business"

class Id(models.Model):
    govid = models.CharField(max_length=8, choices=ID_CHOICES)
    upid=models.ImageField(upload_to='ID/',default='b.jpg')

    def __str__(self):
        return self.govid

    class Meta():
        db_table="Id"

class Company(models.Model):
    bname=models.CharField(max_length=20)
    ctype=models.CharField(max_length=15,choices=COMPANY_CHOICES)

    def __str__(self):
        return self.ctype

    class Meta():
        db_table="Company"

class Information(models.Model):
    location=models.CharField(max_length=15,choices=LOCATION_CHOICES)
    area=models.CharField(max_length=20,choices=AREA_CHOICES)
    eneed = models.IntegerField(choices=INTEGER_CHOICES)
    work=models.CharField(max_length=20,choices=WORK_CHOICES)

    def __str__(self):
        return self.location

    class Meta():
        db_table="Information"

class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

class Domain(models.Model):
    domain = models.CharField(max_length=20)

    def __str__(self):
        return self.domain

    class Meta():
        db_table="Domain"
