
from django.urls import path, include
from .views import CampaignListView, CampaignDetail, SubscribetoCampaign

urlpatterns = [
    path('campaign/', CampaignListView.as_view(), name="campaign"),
    path('campaign/<str:slug>', CampaignDetail.as_view(), name="campaign-detail"),
    path('subscribers/', SubscribetoCampaign.as_view(), name="subscribers"),
]
