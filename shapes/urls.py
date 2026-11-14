"""
URL configuration for shapes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from area.views import SquareView
from area.views import RectangleView
from area.views import TriangleView
from area.views import CircleView
from area.views import ParallelogramView
from area.views import TrapeziumView
from area.views import RhombusView
from area.views import EllipseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('square/',SquareView.as_view()),
    path('rectangle/',RectangleView.as_view()),
    path('triangle/',TriangleView.as_view()),
    path('circle/',CircleView.as_view()),
    path('parallelogram/',ParallelogramView.as_view()),
    path('trapezium/',TrapeziumView.as_view()),
    path('rhombus/',RhombusView.as_view()),
    path('ellipse/',EllipseView.as_view())
]
