from django.db import models


# 都道府県テーブル

class Pref(models.Model):
    code = models.CharField(max_length=2,verbose_name='都道府県コード')
    name = models.CharField(max_length=4,verbose_name='都道府県名')

    def __str__(self):
        return str(self.name)
