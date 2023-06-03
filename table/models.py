from django.db import models
from django.db.models import Min, Avg, Max


class Record(models.Model): #Модель для записи в БД, в которой мы определяем поля
    employee_name = models.CharField(max_length=40)
    raw_material_name = models.CharField(max_length=40)
    iron_concentration = models.FloatField()
    silicon_concentration = models.FloatField()
    aluminum_concentration = models.FloatField()
    calcium_concentration = models.FloatField()
    sulfur_concentration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #То что мы выводим после того как используем модель в .html
        return f"{self.raw_material_name}"
