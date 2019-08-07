from django.forms import ModelForm, Form
from .models import City
from .models import BarberShop
from .models import Masters, TimeForHaircutWoman, TimeForHaircutMan
from django.http import request
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class MasterForm(ModelForm):
    class Meta:

        model = Masters
        fields = ['city', 'barber_shop', 'masters_name', 'telephone_number', 'email', 'man_master', 'woman_master', 'your_photo']


class TimeForHaircutManForm(ModelForm):
    class Meta:
        model = TimeForHaircutMan
        fields = ['man_haircut_short', 'man_haircut_long', 'child_haircut', 'mustache_styling', 'beard_styling']


class TimeForHaircutWomanForm(ModelForm):
    class Meta:
        model = TimeForHaircutWoman
        fields = ['cutting_and_styling_short', 'cutting_and_styling_long1', 'cutting_and_styling_long2',
                'forelock_cutting', 'child_hairstyle', 'styling_long1', 'styling_long2',
                'drying', 'keratin_straightening', 'painting', 'keratin_painting']
