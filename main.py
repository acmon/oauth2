import uvicorn

from fastapi import FastAPI

from routes import breweries, auth, orders

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(auth.router)
app.include_router(breweries.router)
app.include_router(orders.router)

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': [auth]},
    generate_schemas=True,
    add_exception_handlers=True
)

if __name__ == '__main__':
    uvicorn.run(app)