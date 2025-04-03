from fastapi import FastAPI
from app.routers import link_check

app = FastAPI()
app.include_router(link_check.router)

@app.get("/")
def read_root():
    return {"message": "百度网盘链接检测服务"}