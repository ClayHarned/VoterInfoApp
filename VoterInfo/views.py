# VoterInfo/views.py
from django.views.generic import TemplateView

class MyInfoPageView(TemplateView):
    template_name = 'MyInfo.html'

class NextElectionPageView(TemplateView):
    template_name = 'NextElection.html'

class CurrentSeatsPageView(TemplateView):
    template_name = 'CurrentSeats.html'

class PoliticianProfilesPageView(TemplateView):
    template_name = 'PoliticianProfiles.html'

class VotingStatisticsPageView(TemplateView):
    template_name = 'VotingStatistics.html'

class VotingQuestionsAndTipsPageView(TemplateView):
    template_name = 'VotingQuestionsAndTips.html'
