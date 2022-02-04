from django import forms
from.models import Booking,City

class BookForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = 'name', 'age', 'address', 'country', 'city', 'bgroup', 'mob'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['city'].queryset=City.objects.none()

        if 'country' in self.data:
            try:
                country_id=int(self.data.get('country'))
                self.fields['city'].queryset=City.objects.filter(country_id=country_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset=self.instance.country.city_set.order_by('name')


