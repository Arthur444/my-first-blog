from django.utils.encoding import python_2_unicode_compatible
import datetime
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.db import models


from django import forms



class produit(models.Model):
    produit_titre = models.CharField(max_length=100 , default ='')
    #produit_lien = models.SlugField(default ='')
    produit_description = models.TextField(blank=True)
    produit_text = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    photo = models.ImageField(upload_to="photos/" , default ='')
    produit_video = models.TextField(blank=True)
    #pause = models.DurationField(default=timedelta(minutes=20))    
    def __str__(self):
        return self.produit_titre

    def was_published_recently(self):
        now = timezone.now()
        return 0==0 #now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'















#image supplementaires
class Image(models.Model):
    produit = models.ForeignKey(produit, on_delete=models.CASCADE , default ='')
    picture = models.ImageField(upload_to="photos/")
    def __img__(self):
        return self.picture













class Slide(models.Model):
    slide_titre = models.CharField(max_length=100 , default ='')
    pub_date = models.DateTimeField('date published', default=datetime.now)
    photo = models.ImageField(upload_to="diapo/" , default ='')
    def __str__(self):
        return self.slide_titre
        print(photo)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    

























class windsurf(models.Model):
    windsurf_titre = models.CharField(max_length=100 , default ='')
    #windsurf_lien = models.SlugField(default ='')
    windsurf_description = models.TextField(blank=True)
    windsurf_text = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    photo = models.ImageField(upload_to="photos/" , default ='')
    windsurf_video = models.TextField(blank=True)
    #pause = models.DurationField(default=timedelta(minutes=20))    
    def __str__(self):
        return self.windsurf_titre

    def was_published_recently(self):
        now = timezone.now()
        return  0==0 #now - datetime.timedelta.days <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'



class windsurfImage(models.Model):
    windsurf = models.ForeignKey(windsurf, on_delete=models.CASCADE , default ='')
    picture = models.ImageField(upload_to="photos/")
    def __img__(self):
        return self.picture







"""
    
    
    @python_2_unicode_compatible  # only if you need to support Python 2
    class Choice(models.Model):
    produit = models.ForeignKey(produit, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    return self.choice_text
    

    
    
    
    
    
class Product(models.Model):
    product_titre = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/")
    product_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.produit_titre
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'












class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


    """


