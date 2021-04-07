from django.db import models
from sugartsa.models import Pref

def get_default_pref():
    return Pref.objects.get(code='13').pk

# 店舗テーブル
class Shop(models.Model):
    name_kn = models.CharField(max_length=100, verbose_name='店舗名カナ')
    name_kj = models.CharField(max_length=100, verbose_name='店舗名漢字')
    tel = models.CharField(max_length=20, verbose_name='電話番号')
    fax = models.CharField(max_length=20, verbose_name='FAX番号')
    zip = models.CharField(max_length=7, verbose_name='郵便番号')
    pref_id = models.ForeignKey(Pref, on_delete=models.CASCADE, verbose_name='都道府県',
                                default=get_default_pref)
    address_1 = models.CharField(max_length=100, verbose_name='市区郡')
    address_2 = models.CharField(max_length=100, verbose_name='住所番地')
    bld = models.CharField(max_length=100, verbose_name='建物等')

#TODO 店舗テーブル継続