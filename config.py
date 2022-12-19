from typing import List, Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    PROJECT_NAME: str = "perfect-evolution"
    PROJECT_TITLE: str = "perfect-evolution"
    PROJECT_DESCRIPTION: str = "kahoot application"
    PROJECT_VERSION: str = "1.0.0"

    ENCODING: str = 'utf-8'
    
    ADMIN_TITLE: str = "Admin microservice application"
    ADMIN_DESCRIPTION: str = "Admin microservice application description"
    PRIMARY_API_V1_PREFIX: str = "/api/v1"
    AUTH_API_V1_PREFIX: str = "/api/v1/auth"
    ADMIN_API_V1_PREFIX: str = "/api/v1/admin" 
    ACCESS_TOKEN_EXPIRE_MINUTES: int =30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int =60 * 24 * 7 # 7 days
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_SECRET_KEY: str = "MySuperSecret"
    JWT_REFRESH_SECRET_KEY: str = "MySuperSecretRefresh"
    TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    AUTH_EXCLUDE_PATHS: List[str] = [
        "/docs",
        "/redoc",
        "/openapi",
        "/auth/login",
        "/register",
    ]

    LOG_LEVEL: str = "DEBUG"
    LOG_FORMAT: str = (
        "time: {time:YYYY-MM-DD HH:mm:ss Z} | "
        "level: {level} | "
        "request_id: {extra[request_id]} | "
        "user: {extra[user]} | "
        "user_host: {extra[user_host]} | "
        "user_agent: {extra[user_agent]} | "
        "url: {extra[path]} | "
        "method: {extra[method]} | "
        "request_data: {extra[request_data]} | "
        "response_data: {extra[response_data]} | "
        "response_time: {extra[response_time]} | "
        "response_code: {extra[response_code]} | "
        "message: {message} | "
        "exception: {exception}"
    )
    DB_ECHO_LOG: bool = True
    
    DBAUTH: bool = False
    DBURL: Optional[str] = 'mongodb://empedus.services:49694/?retryWrites=true&w=majority'
    DBPORT: int = 49694
    DBHOST: str = "empedus.services"
    DBTYPE: str = "mongodb"
    DBNAME: str = "perfect-evolution"
    DB_USERNAME: Optional[str]
    DB_PASSWORD: Optional[str]



settings = Settings()

print(settings,"@@@")