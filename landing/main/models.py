from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


PR_MANAGEMENT = 'PR'
RISKS_SAFETY = 'RS'
OTHER = 'OTH'
DEPARTMENTS = [
            (PR_MANAGEMENT, 'PR и маркетинг'),
            (RISKS_SAFETY, 'Риски и безопасность'),
            (OTHER, 'Другое')
        ]


class Client(models.Model):

    full_name = models.CharField(
        'Ф.И.О.',
        max_length=256,
    )
    company = models.CharField(
        'Компания',
        max_length=256,
    )
    department = models.CharField(
        'Подразделение',
        max_length=3,
        choices=DEPARTMENTS,
    )
    email = models.EmailField(
        'Email',
        unique=True,
    )
    phone = PhoneNumberField(
        'Телефон',
        unique=True,
    )
    pd_agreement = models.BooleanField(
        'Согласен на обработку ПД',
    )
    in_mailing_list = models.BooleanField(
        'Согласен на рассылку',
    )
