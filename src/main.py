from fastapi import FastAPI
from src.functional import primeNumbersFunc

app = FastAPI()


@app.get("/prime_numbers/{num}")
def prime_numbers(num: int) -> dict[str, int]:
    return {"num": primeNumbersFunc(num)}
