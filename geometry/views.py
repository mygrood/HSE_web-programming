from django.shortcuts import render
from django.http import HttpResponse
import math

#прямоугольник
def get_rectangle_area(request, width, height):
    area = width * height
    return HttpResponse(f"Площадь прямоугольника: {area}")

#квадрат
def get_square_area(request, width):
    area = width * width
    return HttpResponse(f"Площадь квадрата: {area}")

#круг
def get_circle_area(request, radius):
    area = math.pi * (radius ** 2)
    return HttpResponse(f"Площадь круга: {area:.2f}")
