from django.forms import inlineformset_factory, ModelForm

from .models import Speaker, Talk

class SpeakerForm(ModelForm):
    class Meta:
        model  = Speaker
        fields = ['name', 'email', 'email_confirmed', 'bio', 'photo']

SpeakerFormSet = inlineformset_factory(Speaker, Talk, form = SpeakerForm)

class TalkForm(ModelForm):
    class Meta:
        model = Talk
        fields = ['title', 'description', 'talk_type', 'q_and_a', 'speakers']

TalkFormSet = inlineformset_factory(Profile)
