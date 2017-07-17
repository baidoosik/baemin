from .models import Item,Shop,Order
from django import forms


class OrderModelForm(forms.ModelForm):
    def __init__(self, shop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shop = shop
        self.fields['item_set'].queryset = self.fields['item_set'].queryset.filter(shop=shop)


    class Meta:
        model = Order
        fields = ('item_set',)
