from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict


class TeamsView(APIView):
    def post(self, request):
        team_data = request.data

        team = Team(
            name=team_data["name"],
            titles=team_data["titles"],
            top_scorer=team_data["top_scorer"],
            fifa_code=team_data["fifa_code"],
        )

        if "founded_at" in team_data:
            team.founded_at = team_data["founded_at"]

        team.save()

        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()
        # teams_dict = []
        # for team in teams:
        #     t = model_to_dict(team)
        #     teams_dict.append(t)
        return Response(teams.values(), 200)


class TeamsIdView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)

        repr = team.__repr__
        print(repr)
        return Response(model_to_dict(team), 200)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)

        team_data = request.data

        if "name" in team_data.keys():
            team.name = team_data["name"]
        if "titles" in team_data.keys():
            team.titles = team_data["titles"]
        if "top_scorer" in team_data.keys():
            team.top_scorer = team_data["top_scorer"]
        if "fifa_code" in team_data.keys():
            team.fifa_code = team_data["fifa_code"]
        if "founded_at" in team_data.keys():
            team.founded_at = team_data["founded_at"]

        team.save()

        return Response(model_to_dict(team), 200)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)
        team.delete()
        return Response("", 204)
