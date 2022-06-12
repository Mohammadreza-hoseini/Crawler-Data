# from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from rest_framework.permissions import IsAuthenticated

from .models import Companies, EsgScore
import ast
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CompaniesSerializer
from django.core import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def corps(request):
    url = 'https://www.refinitiv.com/en/sustainable-finance/diversity-and-inclusion-top-100#full-list'
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    companies = []
    company = []
    td = content.findAll('td')
    for i in td:
        td_text = i.text
        companies.append(td_text.strip())
    i = 0
    for item in companies:
        i += 1
        company.append(item)
        if i % 5 == 0:
            Companies.objects.create(
                CompanyRank=company[0],
                CompanyName=company[1],
                Industry=company[2],
                Country=company[3],
                Score=company[4]
            )
            company.clear()
            continue
    all_companies = Companies.objects.all()
    ser_data = CompaniesSerializer(instance=all_companies, many=True)
    return Response(data=ser_data.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def esg_score(request):
    name = request.data['name']
    payload = {'ricCode': name}
    r = requests.get("https://www.refinitiv.com/bin/esg/esgsearchresult?", params=payload)
    content = r.text
    dicts = ast.literal_eval(content)
    obj = EsgScore.objects.create(
        Name=name,
        Score=dicts['esgScore']['TR.TRESG']['score'],
        Rank=dicts['industryComparison']['rank'],
        Environment=dicts['esgScore']['TR.EnvironmentPillar']['score'],
        Social=dicts['esgScore']['TR.SocialPillar']['score'],
        Governance=dicts['esgScore']['TR.GovernancePillar']['score']
    )
    serialized_object = serializers.serialize('json', [obj, ])
    print(serialized_object)
    return Response(serialized_object, status=200)
