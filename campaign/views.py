from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Campaign, Subscriber
from .serializers import CampaignSerializer, SubscriberSerializer
# Create your views here.


class CampaignListView(generics.ListAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaign.objects.all()


class CampaignDetail(generics.GenericAPIView):
    def get(self, request, slug):
        query_set = Campaign.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(CampaignSerializer(query_set).data)
        return response.Response("No Data Found", status=status.HTTP_404_NOT_FOUND)


class SubscribetoCampaign(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        return Subscriber.objects.all()
