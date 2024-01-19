import uvicorn
from fastapi import FastAPI

from routers.user_api import user
from routers.websocket_api import ws
from routers.graphql_api import router as graphql_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(user)
app.include_router(ws)
app.include_router(graphql_router)

if __name__ == "__main__":
    uvicorn.run(app, port=10000)