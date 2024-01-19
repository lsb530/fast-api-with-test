import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.routing import Route
from fastapi import APIRouter

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    goodbye = graphene.String(name=graphene.String(default_value="stranger"))
    def resolve_hello(self, info, name):
        return f"Hello {name}"

    def resolve_goodbye(self, info, name):
        return f"Goodbye {name}"

schema = graphene.Schema(query=Query)

graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

router = APIRouter()
router.routes.append(Route("/graphql", endpoint=graphql_app))
