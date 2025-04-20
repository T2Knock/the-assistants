from fastapi import FastAPI
from routers import routers

app = FastAPI(title="The Assistant", version="1.0.0")


@app.get("/")
def read_root():
    return {"pong": True}


for router in routers:
    app.include_router(router)
