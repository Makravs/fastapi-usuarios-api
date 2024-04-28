from fastapi import FastAPI
from db.db import client
from controller.usuarioCRUD import router as usuarios_router

app = FastAPI()
app.include_router(usuarios_router, tags=["usuarios"], prefix="/usuarios")

@app.on_event("shutdown")
async def shutdown_db_client():
    await client.close()