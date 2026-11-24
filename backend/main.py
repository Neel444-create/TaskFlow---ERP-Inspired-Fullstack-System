
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.tasks import router as tasks_router

# 1. Create FastAPI application FIRST
app = FastAPI(title="TaskFlow API")

# 2. Configure CORS AFTER creating app
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Register API routers
app.include_router(auth_router)
app.include_router(tasks_router)


# 4. Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}
