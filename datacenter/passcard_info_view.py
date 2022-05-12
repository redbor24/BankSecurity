from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard_visits = []
    for passcard_visit in Visit.objects.filter(passcard__passcode=passcode):
        passcard_visits.append({
                'entered_at': passcard_visit.entered_at,
                'duration': passcard_visit.format_duration(passcard_visit.get_duration()),
                'is_strange': 'да' if passcard_visit.is_visit_long() else 'нет'
            }
        )
    context = {
        'passcard': Passcard.objects.get(passcode=passcode),
        'this_passcard_visits': passcard_visits
    }
    return render(request, 'passcard_info.html', context)
