from fastapi import FastAPI
from routers import products, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users_db.router)
app.include_router(jwt_auth_users.router)

#Static files
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/", tags= ["Home"])
async def root():
    return 'Hola Mundo!'

@app.get("/message", tags= ["Home"])
async def message():
    return {"message": "Hola fastapi"}