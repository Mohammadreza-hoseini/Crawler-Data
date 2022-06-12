from django.urls import path
from crawlering import views

urlpatterns = [
    path('corps/', views.corps),
    path('esgscore/company_ticker/', views.esg_score),
]
