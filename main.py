from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Employee Management API")

# include routes
app.include_router(router)
