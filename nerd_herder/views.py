from django.shortcuts import render


def code_of_conduct(request):
    return render(request, 'code_of_conduct.html', {'title': 'Code of Conduct'})


def code_of_conduct_reporting_guide(request):
    context = {'title': 'Code of Conduct - Reporting Guide'}
    return render(request, 'code-of-conduct-reporting-guide.html', context)


def code_of_conduct_response_playbook(request):
    context = {'title': 'Code of Conduct - Response Playbook'}
    return render(request, 'code-of-conduct-response-playbook.html', context)


def index(request):
    return render(request, 'index.html')
