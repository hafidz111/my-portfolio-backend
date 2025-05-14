from django.db import models
from django.core.exceptions import ValidationError

class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(default="https://example.com/default-cv.pdf")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk and Profile.objects.exists():
            raise ValidationError("Only one Profile instance is allowed.")
        super().save(*args, **kwargs)

class About(models.Model):
    description = models.TextField()
    github = models.URLField()
    linkedin = models.URLField()
    link = models.URLField(default="https://via.placeholder.com/300")

    def __str__(self):
        return self.description
    
    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValidationError("Only one About instance is allowed.")
        super().save(*args, **kwargs)

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return f"{self.title} - {self.issuer}"
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return f"{self.title} at {self.institution}"
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default="#000000") 
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imageUrl = models.URLField()
    link = models.URLField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return self.title
