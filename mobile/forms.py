from django.forms import ModelForm
from .models import Mobile


class CreateMobileForm(ModelForm):

    class Meta:
        model = Mobile
        fields = "__all__"


    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('mobile_price')

        if price<1000:
            msg = "invalid price provide value > 50"
            self.add_error("mobile_price", msg)












class UpdateMobileForm(ModelForm):

    class Meta:
        model = Mobile
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('mobile_price')

        if price < 1000:
            msg = "invalid price provide value > 50"
            self.add_error("mobile_price", msg)

