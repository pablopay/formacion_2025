from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRAN', 'Transport'),
        ('ENTR', 'Entertainment'),
        ('UTIL', 'Utilities'),
        ('OTHR', 'Other'),
    ]

    description = models.CharField(max_length=225, verbose_name=_('Description'), verbose_name_plural=_('Descriptions'))
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)  # auto_created no es válido aquí
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)


class Meta:
    verbose_name =_('Expense')
    verbose_name_plural = _('Expenses')
    ordering = ['-date']
   

    def __str__(self):
        return f"{self.description} - {self.category} - {self.date}"
