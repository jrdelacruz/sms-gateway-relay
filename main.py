from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/v1/broadcast")
async def echo_payload(request: Request):
    payload = await request.json()
    print("Received payload:", payload)
    return payload

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)