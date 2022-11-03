import uvicorn
from app.api import api_router
from app.core.config import settings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from app.pre_start import init

# init()  # Wait for db + create superuser

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}{settings.API_V1_STR}/openapi.json",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)

if __name__ == "__main__":
    # import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)
