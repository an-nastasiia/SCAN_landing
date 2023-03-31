from django.db import models
from django.core.validators import RegexValidator
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
    email = models.EmailField('Email')
    phone = models.CharField(
        'Телефон',
        max_length=12,
        validators=(
            RegexValidator(regex='^(\+7)[\d\- ]{10}$'),
            )
        )
    pd_agreement = models.BooleanField('Согласен на обработку ПД')
    in_mailing_list = models.BooleanField('Согласен на рассылку')
