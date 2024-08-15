from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "BC4M"}


@app.post("/")
def post(body: dict):
    return body


@app.get("/health")
def health():
    return {"msg": "OK"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=2000)