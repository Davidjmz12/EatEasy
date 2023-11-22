from django.forms import ModelForm

from main.models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rate', 'comment']

    def save(self, commit=True, client_id=None, dish_id=None, date=None):
        rate = super(RatingForm, self).save(commit=False)
        if commit and client_id and dish_id:
            rate.client = client_id
            rate.dish = dish_id
            rate.date = date
            ratings = Rating.objects.filter(client_id=client_id.id, dish_id=dish_id.id).all()
            if(len(ratings)==0):
                rate.save()
        return rate

