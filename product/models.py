from django.db import models

from page.models import DEFAULT_STATUS,STATUS

GENDER_CHOICE=[ 
    ("man","Erkek"),
    ("woman","Kadin"),
    ("unisex","Unisex"),
]
# Create your models ürün.
class Category(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    slug = models.SlugField(
        max_length=200,
        default=""
        ) 


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
    
    gender = models.CharField(
        max_length=6,
        default="unisex",
        choices=GENDER_CHOICE
    )

    createt_at = models.DateTimeField(auto_now_add= True)#auto_now_add eklendiği zaman
    updated_at = models.DateTimeField(auto_now=True)#auto_now her zaman

    def __str__(self):
        return f"{self.pk} - {self.gender} - {self.title}"
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True,null=True)
    slug = models.SlugField(
        max_length=200,
        default=""
        ) 


    cover_image = models.ImageField(
        upload_to = "carousel",
        null=True,
        blank=True,
    )
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    is_home = models.BooleanField(default=False)

    status = models.CharField(
        default = "draft",
        choices=STATUS,
        max_length=10
        ) 

    def __str__(self):
        return self.title
    createt_at = models.DateTimeField(auto_now_add= True)#auto_now_add eklendiği zaman
    updated_at = models.DateTimeField(auto_now=True)#auto_now her zaman


