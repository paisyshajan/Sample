from django.db import models

# Create your models here.

Materials = (('dc', 'Debit_card'), ('cc', 'credit_card'), ('cb', 'checkbook'))
Account_type=(('current','current'),('savings','savings'))
# State=(('Andhra','Andhra'),('Maharashtra','Maharashtra'))
# District=(('Hydhrabadh','Hydhrabadh'),('Pune','Pune'),('Mumbai','Mumbai'))
# Branch=(('Hyd_1','Hydra_2'),('Pune_1','Pune_1'))
# # State=(('Kerala','Kerala'),('Tamilnadu','Tamilnadu'),(''))


# class State(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name

class District(models.Model):

    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Branch(models.Model):

    name = models.CharField(max_length=30)

    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age=models.TextField(max_length=50)
    address=models.TextField(max_length=250)
    dob = models.DateField(null=True, blank=True)

    district = models.ForeignKey(District,on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    gender = models.TextField(choices=[('male', 'Male'), ('female', 'female')])
    phone = models.IntegerField()
    email = models.TextField(max_length=100)

    account=models.CharField(choices=Account_type,max_length=100)
    materials=models.CharField(choices=Materials,max_length=100)


    def __str__(self):
        return '{}'.format(self.name)
