from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import Client, DEPARTMENTS


class ClientSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(
        max_length=256,
        required=True,
        label='Ваше ФИО',
        style={'template': 'input_required.html'},
    )
    company = serializers.CharField(
        max_length=256,
        required=True,
        label='Компания',
        style={'template': 'input_required.html'},
        )
    department = serializers.ChoiceField(
        choices=DEPARTMENTS,
        required=True,
        label='Подразделение',
        style={'template': 'select_required.html'},
        )
    email = serializers.EmailField(
        required=True,
        label='Ваш рабочий Email',
        style={'template': 'input_required.html'},
    )
    phone = PhoneNumberField(
        required=True,
        label='Телефон',
        style={'template': 'input_required.html',
               'input_type': 'tel',
               'placeholder': '+7XXXXXXXXXX'},
    )
    pd_agreement = serializers.BooleanField(
        required=True,
        label='Соглашаюсь на обработку песональных данных в соответствии с',
        style={'template': 'checkbox_required.html'},
    )
    in_mailing_list = serializers.BooleanField(
        required=False,
        label='Соглашаюсь получать рассылку от «СКАН-Интерфакс»',
    )

    class Meta:
        model = Client
        fields = (
            'full_name', 'company',
            'department', 'email', 'phone',
            'pd_agreement', 'in_mailing_list',
        )
