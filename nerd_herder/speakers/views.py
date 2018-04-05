from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import TalkForm, SpeakerForm

# create a form where for the user to enter their data re: their talk
def talk_form(request):
    talk_form = TalkForm(prefix="talk")
    speaker_form = SpeakerForm(prefix="speaker")

    if request.POST:
        talk_form = TalkForm(request.POST, prefix="talk")
        speaker_form = SpeakerForm(request.POST, prefix="speaker")
        print('foo')

        if talk_form.is_valid() and speaker_form.is_valid():
            talk = talk_form.save(commit=False)
            talk.speaker = speaker_form.save()
            print('blah')

            talk.save()
            # TODO make it redirect
            return redirect('talk_overview', talk.id)

    return render(request, 'talk_detail.html', {'talk': talk_form, 'speaker':speaker_form})

#function to display the contents of what the user submitted, for review
def talk_confirmation(request, talk_id):
    return render(request, 'talk_confirmation.html', {'talk_id':talk_id})
    # use the identifier (talk_id) to get an instance of the talk model
    #

# def confirmation(request, talk_id):
#     conf_talk_form = TalkForm()
#     conf_speaker_form = SpeakerForm()
#
#     formresult= ''
#
#     if request.method == 'POST':
#         talkresult1 = TalkForm(request.POST)
#         speakerresult = SpeakerForm(request.POST)
#
#         if formresult.is_valid():
#             return HttpResponseRedirect('talk_confirmation.html')
#
#     context= { 'conf_talk_form': conf_talk_form, 'conf_speaker_form':conf_speaker_form }
#
#     return render(request, 'talk_confirmation.html', context)
