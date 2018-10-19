from django import forms


class VoteForm(forms.Form):
    VOTE_CHOICES = (('1', 'Mitch'), ('2', 'Mike'), ('3', 'Steve'))
    vote = forms.ChoiceField(widget=forms.RadioSelect, choices=VOTE_CHOICES)