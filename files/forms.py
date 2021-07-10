from django import forms
class AuthForm(forms.Form):
    code = forms.CharField(label='Auth Code', max_length=16)
    class Meta:
        fields = (
          'code',
        )
