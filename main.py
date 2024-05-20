import httpx
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request

app = FastAPI()

load_dotenv()

@app.post("/v1/broadcast")
async def send_sms(request: Request):
    data = await request.json()
    payload = {
        "recipient": data['recipient'],
        "message": data['body']
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{os.getenv('SMS_GATEWAY_URL')}/v1/broadcast",
            headers={"x-api-key": os.getenv('SMS_GATEWAY_KEY')},
            json=payload
        )
    message = {"status": response.status_code, "message": response.text}
    print(message)
    return message
