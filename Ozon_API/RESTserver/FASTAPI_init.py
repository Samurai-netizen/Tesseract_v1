from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from pyngrok import ngrok
import uvicorn, nest_asyncio
from datetime import datetime
import hmac
import hashlib
from config import HEADERS

from Telegram_API.chat_DB import fetchTelegramID
from Telegram_API.handlers.indep_transfer import message_sender


http_tunnel = ngrok.connect(8000)

print(f"Public URL: {http_tunnel.public_url}")

headers = HEADERS

app = FastAPI()


def generate_signature(data, secret_key):

    sign_string = json.dumps(data)

    signature = hmac.new(secret_key.encode(), sign_string.encode(), hashlib.sha256).hexdigest()

    return signature


errors = {
    "EMPTY_SIGN": {"error": "EMPTY_SIGN", "message": "Подпись отсутствует"},
    "INVALID_SIGN": {"error": "INVALID_SIGN", "message": "Неверная подпись"},
    "WRONG_PUSH_TYPE": {"error": "WRONG_PUSH_TYPE", "message": "Неверный тип уведомления"},
    "WRONG_BODY": {"error": "WRONG_BODY", "message": "Неверное тело уведомления"},
    "EMPTY_BODY": {"error": "EMPTY_BODY", "message": "Пустое тело уведомления"}
}

result200 = {
  "result": True
}

forError = {
  "error": {
    "code": "400",
    "message": "ошибка",
    "details": "намеренная ошибка от озона"
  }
}

dashes = '--------------------------------------------------------------------------'

@app.post("/TYPE_PING")
async def alert(request: Request):
    print('')
    print(dashes)
    body = await request.body()

    # Проверка пустого тела
    if not body:
        print('Ошибка: ', errors["EMPTY_BODY"])
        print('Время: ', datetime.utcnow().isoformat(sep='T', timespec='seconds'))
        print(dashes)
        return JSONResponse(content=errors["EMPTY_BODY"], status_code=400, headers=headers)

    try:
        json_data = json.loads(body.decode())
    except json.JSONDecodeError as e:
        print("JSON crashed")
        print(body)
        print('Ошибка: ', errors["WRONG_BODY"])
        print('Время: ', datetime.utcnow().isoformat(sep='T', timespec='seconds'))
        print(dashes)
        return JSONResponse(content=errors["WRONG_BODY"], status_code=400, headers=headers)

    # Проверка подписи
    #if "sign" not in json_data or not json_data["sign"]:
        #print("sign error")
        #return JSONResponse(content=errors["EMPTY_SIGN"], status_code=400, headers=headers)

    # Проверка типа уведомления
    #if "message_type" not in json_data or json_data["message_type"] != "TYPE_PING":
        #return JSONResponse(content=errors["WRONG_PUSH_TYPE"], status_code=400, headers=headers)

    match json_data["message_type"]:
        case 'TYPE_PING':
            print("TEST REQUEST = TYPE_PING was sent")
            current_time_utc = datetime.utcnow().isoformat(timespec='seconds') + "Z"
            print(current_time_utc)
            TYPE_PINGResult200 = {
                "version": "string",
                "name": "string",
                "time": current_time_utc
            }

            print('Успех')
            print('Время: ', datetime.utcnow().isoformat(sep='T', timespec='seconds'))
            print(dashes)
            return JSONResponse(content=TYPE_PINGResult200, status_code=200, headers=headers)

        case 'TYPE_STOCKS_CHANGED':
            print(body)
            id = fetchTelegramID(HEADERS['Client-Id'])
            await message_sender(id, str(body))
            print('Успех')
            print('Время: ', datetime.utcnow().isoformat(sep='T', timespec='seconds'))
            print(dashes)
            return JSONResponse(content=result200, status_code=200, headers=headers)

        case 'TYPE_NEW_MESSAGE':
            print(body)
            id = fetchTelegramID(HEADERS['Client-Id'])
            await message_sender(id, str(body))
            print('Успех')
            print('Время: ', datetime.utcnow().isoformat(sep='T', timespec='seconds'))
            print(dashes)
            return JSONResponse(content=result200, status_code=200, headers=headers)

        case _:
            print("Something else happened...")
            print('Ошибка: ', errors["WRONG_PUSH_TYPE"])
            print('Время: ', datetime.utcnow().isoformat(sep='T', timespec='seconds'))
            print(dashes)
            return JSONResponse(content=errors["WRONG_PUSH_TYPE"], status_code=400, headers=headers)


nest_asyncio.apply()
uvicorn.run("FASTAPI_init:app", port=8000)