from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .validators import validate_time
from .fields import TimeForCuttingField


# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class BarberShop(models.Model):
    barber_shop = models.CharField(max_length=30)
    address = models.CharField(max_length=70)

    def __str__(self):
        return self.barber_shop


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.user


class Masters(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    #id = models.AutoField(primary_key=True)
    #user = models.CharField(max_length=50)
    #user = models.F(get_user_model(), on_delete=models.CASCADE)

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    barber_shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE)
    masters_name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=13)
    email = models.EmailField()
    man_master = models.BooleanField()
    woman_master = models.BooleanField()
    your_photo = models.ImageField(upload_to='images')
#

    def __str__(self):
        return str(self.city) + ' ' + str(self.barber_shop) + ' ' + str(self.masters_name)

    #' '.join(self.city, self.barber_shop, self.masters_name)


class TimeForHaircutMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    man_haircut_short = TimeForCuttingField()
    man_haircut_long = models.IntegerField(validators=[validate_time])
    child_haircut = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    mustache_styling = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    beard_styling = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])


class TimeForHaircutWoman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    cutting_and_styling_short = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    cutting_and_styling_long1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    cutting_and_styling_long2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    forelock_cutting = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    child_hairstyle = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    styling_long1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    styling_long2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    drying = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    keratin_straightening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    painting = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
    keratin_painting = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(180)])
