from django import forms

class PredictForm(forms.Form):

    GENDER = [
        (0, 'Laki - Laki'),
        (1, 'Perempuan')
    ]

    MENARIK = [
        (1, 'Ya'),
        (0, 'Tidak')
    ]

    RAMAI = [
        (1, 'Ya'),
        (0, 'Tidak')
    ]

    DISKON = [
        (1, 'Ya'),
        (0, 'Tidak')
    ]

    gender = forms.ChoiceField(choices=GENDER, required=True, label='Gender', widget=forms.Select(attrs={'class': 'select-field'}))
    menarik = forms.ChoiceField(choices=MENARIK, required=True, label='Menarik', widget=forms.Select(attrs={'class': 'select-field'}))
    ramai = forms.ChoiceField(choices=RAMAI, required=True, label='Ramai', widget=forms.Select(attrs={'class': 'select-field'}))
    diskon = forms.ChoiceField(choices=DISKON, required=True, label='Diskon', widget=forms.Select(attrs={'class': 'select-field'}))