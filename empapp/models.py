from django.db import models

# Create your models here.

GENDER_CHOICES=(('M','Male'), ('F','Female')
                )
COMPANY_CHOICES=[('web design','Web Design'),('sales & marketing','Sales & Marketing'),('software','Software'), ('php','PHP'),
               ('networking','Networking')
]
JOB_CHOICES=[('full time','Full Time'), ('part time','Part Time'), ('work at home','Work from Home')
]
COUNTRY_CHOICES=[('india','India'), ('canada','Canada'), ('uk','UK'), ('australia','Australia')
]
class Employee(models.Model):
    name=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,)
    c_name=models.CharField(max_length=50,choices=COMPANY_CHOICES,)
    j_type=models.CharField(choices=JOB_CHOICES,max_length=20)
    mobile_n=models.IntegerField()
    address=models.CharField(max_length=50)
    country=models.CharField(choices=COUNTRY_CHOICES,max_length=50)
    resume=models.FileField(upload_to='resume/',default='xyz.pdf')

    def __str__(self):
        return self.name

    class Meta():
        db_table="Employee"
