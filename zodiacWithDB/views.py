from django.shortcuts import render, get_object_or_404
from .models import ZodiacSign


#список
def zodiac_list(request):
    signs = ZodiacSign.objects.all()
    return render(request, 'zodiacWithDB/zodiac_list.html', {'signs': signs})


#конкретный знак
def zodiac_detail(request, sign_id):
    #если sign_id не может быть преобразован в int - ValueError и перекинет в 404
    #если не найдена запись по id - DoesNotExist и перекинет в 404
    try:
        sign_id = int(sign_id)
        sign = ZodiacSign.objects.get(id=sign_id)
        return render(request, 'zodiacWithDB/zodiac_detail.html', {'sign': sign})
    except (ZodiacSign.DoesNotExist, ValueError):
        return render(request, 'zodiacWithDB/404.html', status=404)

