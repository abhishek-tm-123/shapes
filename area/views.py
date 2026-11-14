from django.shortcuts import render
from django.views.generic import View

from json import loads 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from math import pi
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class SquareView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        a=form_data.get("side")
        area = a**2
        response_data = {
            "square_area":area
        }

        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class RectangleView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        l=form_data.get("length")
        w=form_data.get("width")
        area = l*w
        respoanse_data = {
            "rectangle_area":area
        }
        return JsonResponse(respoanse_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class TriangleView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        area=(0.5)*b*h
        response_data = {
            "triangle_area":area
        }
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class CircleView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        r = form_data.get("radius")
        area = pi*r*r
        response_data = {
            "circle_area":area
        }
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class ParallelogramView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        area = b*h
        response_data = {
            "parallelogram_area":area
        }
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class TrapeziumView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        a=form_data.get("a")
        b=form_data.get("b")
        h=form_data.get("height")
        area = (0.5)*(a+b)*h
        response_data = {
            "trapezium_area":area
        }
        return JsonResponse(response_data)
    
    
@method_decorator(csrf_exempt,name="dispatch")
class RhombusView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        area = b*h
        response_data = {
            "rhombus_area":area
        }
        
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class EllipseView(View):
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        a=form_data.get("a")
        b=form_data.get("b")
        area = pi*a*b
        response_data = {
            "ellipse_data":area
        }
        return JsonResponse(response_data)