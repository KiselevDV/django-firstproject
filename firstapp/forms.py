from django import forms
from .models import Order, Pizza


class OrderForm(forms.ModelForm):
    """Форма для заказа пиццы"""
    # Поле pizza - поле выбора (ModelChoiceField) всех пицц (Pizza.objects.all) в пиццерии
    # HiddenInput - скрывает поле
    pizza = forms.ModelChoiceField(
        queryset=Pizza.objects.all(), widget=forms.HiddenInput)

    class Meta:  # Задаём логику форме c
        model = Order  # model - свойство, Order - из какой модели брать
        fields = ('pizza', 'name', 'phone')  # fields - какие поля