from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField()
    price = models.DecimalField( max_digits=6, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone = models.CharField( max_length=13)
    address = models.CharField(max_length=150)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    arrived_at = models.TimeField(null=True, blank=True)
    left_at = models.TimeField(null = True, blank=True)
    STATUS = (
        ('at time', 'at time'),
        ('late', 'late'),
        ('not came', 'not came'),
    )
    status = models.CharField(choices=STATUS, max_length=50)

class Apsent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE )
    reason = models.TextField()
    
    