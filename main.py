from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sum")
async def calculate(a: float, b: float):
    return {"a": a, "b": b, "sum": a + b}
