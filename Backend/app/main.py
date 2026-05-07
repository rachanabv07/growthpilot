
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.webhook import router as webhook_router
from app.routes.router_jobs import router as jobs_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(webhook_router)
app.include_router(jobs_router)

app.mount(
    "/generated",
    StaticFiles(directory="generated"),
    name="generated"
)

@app.get("/")
def root():
    return {"message": "GrowthPilot AI running"}
