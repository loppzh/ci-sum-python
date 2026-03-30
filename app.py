from fastapi import FastAPI

app = FastAPI()


def sum_values(a: int, b: int) -> int:
    return a + b


def subtract_values(a: int, b: int) -> int:
    return a - b


@app.get("/")
def read_root():
    return {"message": "API de soma funcionando"}


@app.get("/sum/{a}/{b}")
def get_sum(a: int, b: int):
    return {"result": sum_values(a, b)}


@app.get("/subtract/{a}/{b}")
def get_subtract(a: int, b: int):
    return {"result": subtract_values(a, b)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)