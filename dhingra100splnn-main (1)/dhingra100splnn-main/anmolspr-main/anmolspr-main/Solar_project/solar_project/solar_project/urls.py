"""
URL configuration for solar_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from solar_app import views as v1
from solar_app.views import WeeklyDataAPIView
from solar_app.views import RecordsLastSevenDaysView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('solarr/',v1.home_page_view),
    path('api/weekly-data/', WeeklyDataAPIView.as_view(), name='weekly-data'),
    path('api/solar-data/last-seven-days/', RecordsLastSevenDaysView.as_view(), name='records-last-seven-days'),
    
]




