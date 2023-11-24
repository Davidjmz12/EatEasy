from django.forms import ModelForm

from main.models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["comment"]

    def save(self, commit=True, client_id=None, dish_id=None, date=None, rating_v=0):
        rating = super(RatingForm, self).save(commit=False)
        if commit and client_id and dish_id:
            rating.client = client_id
            rating.dish = dish_id
            rating.date = date
            rating.rate = rating_v
            ratings = Rating.objects.filter(
                client_id=client_id.id, dish_id=dish_id.id
            ).all()
            if len(ratings) == 0:
                rating.save()
            else:
                for oneRate in ratings:
                    oneRate.delete()
                rating.save()
        return rating
