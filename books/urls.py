from django.urls import path
from graphene_django.views import GraphQLView
from books.schema import schema


urlpatterns = [
    # Juste une URL pour accéder à l'interface GraphQL
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
