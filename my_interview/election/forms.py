from django import forms

class NewPollingUnit(forms.Form):
    """
    This form resgisters results from a new polling Unit
    """
    polling_unit_id = forms.CharField(max_length=50)
    party_abbreviation = forms.CharField(max_length=4)
    party_score = forms.IntegerField()
    entered_by_user = forms.CharField(max_length=50)
    date_entered = forms.DateTimeField()
    user_ip_address = forms.CharField(max_length=50)

# Field_name = forms.FieldType(attributes)