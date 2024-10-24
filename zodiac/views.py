from dbm import error
from lib2to3.fixes.fix_input import context

from django.shortcuts import render

ZODIAC_SIGNS = [
    {'name': 'Овен', 'description': 'Овен — это знак энергии, стремления и активности. Люди, рожденные под этим знаком, известны своим упорством и смелостью. Они любят быть в центре внимания и часто берут на себя лидерство.', 'image': 'images/aries.jpg'},
    {'name': 'Телец', 'description': 'Телец — это знак стабильности и упорства. Люди, рожденные под этим знаком, ценят комфорт и материальные блага. Они практичны, реалистичны и способны стойко переносить трудности.', 'image': 'images/taurus.jpg'},
    {'name': 'Близнецы', 'description': 'Близнецы — это знак общения и любознательности. Люди, рожденные под этим знаком, обладают быстрым умом и остроумием. Они обожают общаться и исследовать новые идеи.', 'image': 'images/gemini.jpg'},
    {'name': 'Рак', 'description': 'Рак — это знак эмоций и чувствительности. Люди, рожденные под этим знаком, часто заботливы и защитны по отношению к своим близким. Они ценят домашний уют и семейные традиции.', 'image': 'images/cancer.jpg'},
    {'name': 'Лев', 'description': 'Лев — это знак творчества и самовыражения. Люди, рожденные под этим знаком, обладают харизмой и уверенность в себе. Они любят быть в центре внимания и стремятся вдохновлять других.', 'image': 'images/leo.jpg'},
    {'name': 'Дева', 'description': 'Дева — это знак анализа и внимания к деталям. Люди, рожденные под этим знаком, практичны и трудолюбивы. Они стремятся к совершенству и могут быть критичными как к себе, так и к другим.', 'image': 'images/virgo.jpg'},
    {'name': 'Весы', 'description': 'Весы — это знак гармонии и справедливости. Люди, рожденные под этим знаком, ценят красоту и искусство. Они стремятся к равновесию и часто играют роль миротворцев.', 'image': 'images/libra.jpg'},
    {'name': 'Скорпион', 'description': 'Скорпион — это знак глубины и интенсивности. Люди, рожденные под этим знаком, эмоциональны и страстны. Они часто интересуются скрытыми истинами и мистикой.', 'image': 'images/scorpio.jpg'},
    {'name': 'Стрелец', 'description': 'Стрелец — это знак приключений и оптимизма. Люди, рожденные под этим знаком, стремятся к свободе и исследованию. Они открыты для новых идей и имеют широкий кругозор.', 'image': 'images/sagittarius.jpg'},
    {'name': 'Козерог', 'description': 'Козерог — это знак дисциплины и амбициозности. Люди, рожденные под этим знаком, трудолюбивы и нацелены на достижение своих целей. Они практичны и реалистичны.', 'image': 'images/capricorn.jpg'},
    {'name': 'Водолей', 'description': 'Водолей — это знак оригинальности и независимости. Люди, рожденные под этим знаком, стремятся к переменам и прогрессу. Они часто являются новаторами и обладают уникальным взглядом на жизнь.', 'image': 'images/aquarius.jpg'},
    {'name': 'Рыбы', 'description': 'Рыбы — это знак интуиции и чувствительности. Люди, рожденные под этим знаком, творческие и мечтательные. Они обладают глубокой эмпатией и часто могут понимать чувства других.', 'image': 'images/pisces.jpg'},
]

def show_all_signs(request):
    return render(request, 'zodiac/show_all_signs.html', {'signs': ZODIAC_SIGNS})

def show_sign(request, sign_name):
    # Находим знак по имени
    sign = next((s for s in ZODIAC_SIGNS if s['name'] == sign_name), None)
    if sign is None:
        context = {"error": "error"}
        return render(request, 'zodiac/show_sign.html', context)

    context = {'sign': sign,"error": ""}
    return render(request, 'zodiac/show_sign.html', context)
