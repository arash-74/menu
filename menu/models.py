from django.db import models


def image_path(instance, filename):
    path = f'{instance.name}/{filename}'
    return path
# Create your models here.
class Item(models.Model):
    class CategoryChoice(models.IntegerChoices):
        cold_drink = 1 , 'نوشیدنی سرد'
        hot_drink = 2 , 'نوشیدنی گرم'
        soft_drink = 3 , 'نوشیدنی دمی'
        cake = 4, 'کیک'
        meal = 5, 'غذا'
    name = models.CharField(max_length=100)
    category = models.PositiveIntegerField(choices=CategoryChoice.choices,default=None,null=True,blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=image_path)