from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)



class Students(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    bio = models.TextField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_students", null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    mfd = models.DateField()
    best_before = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.item_name


class StudentProfile(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE)

    contact = models.CharField(max_length=20)
    roll_no = models.IntegerField()

class ItemDetail(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    
    price = models.IntegerField()
    color = models.CharField(max_length=20)

    
class Publication(models.Model):
    title = models.CharField(max_length=20)

    def __str__ (self):
        return self.title


class Article (models.Model):
    headliine = models.CharField(max_length=20)
    publications = models.ManyToManyField(Publication)
    def __str__(self):
        return self.headline