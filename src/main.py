from fastapi import FastAPI
import redis
import debugpy

app = FastAPI()

r = redis.Redis(host='redis',port=6379)
# debugpy.listen('0.0.0.0',5678)

@app.get("/")
def read_root():
    return {"Hello Guys: Lets Learn Docker"}


@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}