from django.http import JsonResponse

def index(request):
    data = {
        'name': 'Mike LOGOVI',
        'surname': 'Dresseur de code',
        
    }
    return JsonResponse(data)
