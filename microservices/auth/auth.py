from fastapi import FastAPI
from microservices.auth.routes.v1.JWTAuthentication import jwtauthentication_router
from microservices.auth.middlewares.PrimaryAuthMiddleware import AuthMiddleware
from config import settings

auth_app = FastAPI(
    title=settings.ADMIN_TITLE,
    description=settings.ADMIN_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
)

# ADD MIDDLEWARES
auth_app.add_middleware(middleware_class=AuthMiddleware)

auth_app.include_router(jwtauthentication_router, prefix="/jwt-auth")