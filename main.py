import fastapi
import uvicorn

print("Hello")
api = fastapi.FastAPI()

@api.get('/api/endpoint')
def endpoint():
    return {"msg": 'Hello FastAPI'}

uvicorn.run(api)