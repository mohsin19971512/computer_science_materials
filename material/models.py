from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Branch(models.Model):
    name  = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='branche_pict/')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    course = models.CharField(choices=(("1s","1s"),("2nd","2nd")),max_length=10)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='courses')
    level = models.CharField(choices=(("one","one"),("two","two"),("three","three"),("four","four")),max_length=50)
    subjects = models.ManyToManyField('material.Subject',related_name='courses')

    def __str__(self):
        return f"level {self.level}- {self.course}-{self.branch}"


class Subject(models.Model):
    name = models.CharField(max_length=250)
    units = models.IntegerField(null=True)
    lecture = models.FileField('Lecture', upload_to='lecture/',null=True,blank=True)
    plan = models.FileField('Plan', upload_to='plan/',null=True,blank=True)
    teacher = models.ForeignKey('material.Teacher',on_delete=models.SET_NULL,null=True)
   

    def __str__(self):
        return  f"{self.name}"




#-----------------------------------------------------------------------------
class Academic_Program_Description_Forms(models.Model):
    title = models.CharField(max_length=500)
    content = models.ForeignKey(Subject,null=True,on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Academic Program Description Form"
        verbose_name_plural = "Academic Program Description Forms"
    def __str__(self):
        return  f"{self.title}"


class Course_description_of_common_materials(models.Model):
    stage = models.CharField(choices=(("one","one"),("tow","tow"),("three","three"),("four","four")),max_length=50)
    common_materials = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = "Course description of common material"
        verbose_name_plural = "Course description of common materials"

class Course_Description_of_Specialized_Courses(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    stage = models.CharField(choices=(("one","one"),("tow","tow"),("three","three"),("four","four")),max_length=50)
    materials = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = "Course Description of Specialized Course"
        verbose_name_plural = "Course Description of Specialized Courses"


class Researche(models.Model):
    year = models.DateField(auto_created=True)
    research = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.research}-{self.research.first()}'

#----------------------------------------------------------------------------------------------

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name="Full Name",max_length=255)
    image  = models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    mobile = models.CharField(max_length=40)
    gmail  = models.EmailField(verbose_name="Gmail",null=True,blank=True)
    gender =  models.CharField(choices=(("Male","Male"),("female","female")),max_length=20)
    age = models.IntegerField(verbose_name="Age")
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True,verbose_name="Branch")
    education = models.CharField(verbose_name="Education",max_length=500)
    degree = models.CharField(verbose_name="Degree",max_length=100)
    teacing = models.ManyToManyField(Subject,related_name="teachers")
    honor = models.CharField("Honors And Awards",max_length=500)
    links = models.ForeignKey('material.Linke',on_delete=models.SET_NULL,null=True)
    joindate=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    
class Linke(models.Model):
    google_scholar = models.CharField(verbose_name="Google Scholar",max_length=500)
    research_gate = models.CharField(verbose_name="Research Gate",max_length=500)
    publons = models.CharField(verbose_name="Publons",max_length=500)
    orcid = models.CharField(verbose_name="ORCID",max_length=500)
    scopus = models.CharField(verbose_name="Scopus",max_length=500)
    

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
    full_name = models.CharField(verbose_name="Full Name",max_length=255,null=True)
    mobile = models.CharField(max_length=40,null=True)
    image  = models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    gender =  models.CharField(choices=(("Male","Male"),("female","female")),max_length=20,null=True)
    age = models.IntegerField(verbose_name="Age",null=True)
    branch = models.ForeignKey("material.Branch",on_delete=models.SET_NULL,null=True)
    level = models.CharField(choices=(("one","one"),("tow","tow"),("three","three"),("four","four")),max_length=20,null=True)
    joindate=models.DateField(auto_now_add=True)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url






class Questions_Bank(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    subject = models.FileField('subject', upload_to='questions/',null=True,blank=True)
    year = models.DateField(auto_created=True)
    term = models.CharField(verbose_name="Term",choices=(("First","First"),("Second","Second")),max_length=20)
    solution = models.FileField('Solution', upload_to='questions/',null=True,blank=True)
    level = models.CharField(choices=(("one","one"),("tow","tow"),("three","three"),("four","four")),max_length=50)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    course = models.CharField(choices=(("1st","1st"),("2nd","2nd")),max_length=10)

    def __str__(self) -> str:
        return f'{self.year}'

    class Meta:
        verbose_name = "Questions Bank"




"""
class Teaching_staff(models.Model):
    name = models.CharField(verbose_name="Name",max_length=100)
    department = models.CharField(verbose_name="Department",max_length=100)
    degree = models.CharField(verbose_name="Degree",max_length=100)
    profile = models.ForeignKey('staff.Profile',verbose_name="WorkPlace",null=True,on_delete=models.SET_NULL)
    education = models.CharField(verbose_name="Education",max_length=500)
    research_interests = models.ManyToManyField('staff.ResearchInterest',)
    teacing = models.ManyToManyField('staff.Subject',)
    honor = models.CharField("Honors And Awards",max_length=500)

    class Meta:
        verbose_name = "Teaching staff"
"""