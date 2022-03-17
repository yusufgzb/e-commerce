from django.db import models

DEFAULT_STATUS = "daraft"
STATUS = [
    ('draft',"Taslak"),
    ('published',"Yayinlandi"),
    ('delete',"Silindi"),
]

# Create your models sayfa.


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,default="") 
    convert = models.TextField()
    cover_image = models.ImageField(upload_to="page")
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
        ) 
    createt_at = models.DateTimeField(auto_now_add= True)#auto_now_add eklendiği zaman
    updated_at = models.DateTimeField(auto_now=True)#auto_now her zaman

class Carousel(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    cover_image = models.ImageField(
        upload_to = "carousel",
        null=True,
        blank=True,
    )
    status = models.CharField(
        default = "draft",
        choices=STATUS,
        max_length=10
        ) 
    createt_at = models.DateTimeField(auto_now_add= True)#auto_now_add eklendiği zaman
    updated_at = models.DateTimeField(auto_now=True)#auto_now her zaman