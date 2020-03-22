from django import forms


class LinkForm(forms.Form):
    link_to_game = forms.CharField(label='Link ', required=True)