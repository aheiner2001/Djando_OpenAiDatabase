from django import forms

class QueryForm(forms.Form):
      prompt = forms.CharField(label='Enter your query', max_length=255)
# from django import forms

# class QueryForm(forms.Form):
#     PRESET_CHOICES = [
#         ('', 'Select a preset idea'),  # Default blank option
#         ('idea1', 'show all'),
#         ('idea2', 'Idea 2'),
#         ('idea3', 'Idea 3'),
#         ('custom', 'Custom (Enter Below)')  # Option for custom input
#     ]

#     preset_idea = forms.ChoiceField(choices=PRESET_CHOICES, required=False, label="Choose a preset idea")
#     prompt = forms.CharField(label='Or enter your query', max_length=255, required=False)
