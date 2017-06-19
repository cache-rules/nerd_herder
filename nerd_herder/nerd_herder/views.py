from django.http import HttpResponse


def index(request):
    # TODO: determine what should go on index page.
    #   - Maybe just redirect to talk submit page?
    #   - Maybe guide organizers to login and potential speakers to submit talk page?
    #   - Maybe have index page be information about the meetup?
    return HttpResponse('Welcome to Nerd Herder')
