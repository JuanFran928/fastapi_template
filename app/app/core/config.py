import secrets
from typing import Any, Optional

import app.core.env
from app.core.dsn import MysqlDsn
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_STR: str = "/api"
    API_V1_STR: str = "/v1"
    API_LOGIN_STR: str = f"{API_STR}{API_V1_STR}/login/access-token"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    TOKEN_SIGNATURE_ALGORITHM = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str or list[str]) -> str or list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    
    DB_SCHEMA: str
    DB_SERVER: str
    DB_PORT: str
    
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[MysqlDsn] = None
        
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_users_db_connection(cls, v: Optional[str],
                                     values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return MysqlDsn.build(
            scheme=values.get("DB_SCHEMA", "mysql+pymysql"),
            user=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            host=values.get("DB_SERVER", "localhost"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('MYSQL_DB') or ''}",
        )




    SMTP_TLS: bool = True
    SMTP_PORT: int or None = None
    SMTP_HOST: str or None = None
    SMTP_USER: str or None = None
    SMTP_PASSWORD: str or None = None
    EMAILS_FROM_EMAIL: EmailStr or None = None
    EMAILS_FROM_NAME: str or None = None

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: str or None, values: dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "./app/mail/templates/build"
    EMAILS_ENABLED: bool

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST") and values.get("SMTP_PORT") and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    USERS_OPEN_REGISTRATION: bool

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
