from fastapi import FastAPI

# Example from: https://fastapi.tiangolo.com/tutorial/first-steps/

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

