from django import forms

class GuessWord(forms.Form):
    your_guess = forms.CharField(label='Whats your guess  ', max_length=10)