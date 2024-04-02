from django.db import models

class category(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField(default="")
    image=models.ImageField(upload_to='shop',null=True,blank=True)

    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to='products',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)  #add one time
    updated=models.DateTimeField(auto_now=True)   #add every time
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

