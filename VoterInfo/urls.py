# VoterInfo/urls.py
from django.urls import path
from .views import MyInfoPageView, NextElectionPageView, PoliticianProfilesPageView, CurrentSeatsPageView, VotingStatisticsPageView, VotingQuestionsAndTipsPageView
#was originally 'about/' in first path
urlpatterns = [
    path('VotingQuestionsAndTips/', VotingQuestionsAndTipsPageView.as_view(), name='VotingQuestionsAndTips'),
    path('VotingStatistics/', VotingStatisticsPageView.as_view(), name='VotingStatistics'),
    path('PoliticianProfiles/', PoliticianProfilesPageView.as_view(), name='PolitionProfiles'),
    path('CurrentSeats/', CurrentSeatsPageView.as_view(), name='CurrentSeats'),
    path('NextElection/', NextElectionPageView.as_view(), name='NextElection'),
    path('', MyInfoPageView.as_view(), name='MyInfo')

]
