from .models import PersonalInfo


def personal_info(request):
    info = PersonalInfo.load()
    return {"personal_info": info}
