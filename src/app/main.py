from sqlalchemy.orm import declarative_base

Base = declarative_base()
from urllib.parse import urljoin
from starlette.middleware.cors import CORSMiddleware
from src.app.api.api_v1.api import api_router
# from app.services.auth import get_current_user

# from app.services.get_settings import get_settings
# from app.db.db import Base, engine
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

# @app.get("/users/me")
# async def read_users_me(current_user: Annotated[UserResponse, Depends(get_current_user)]):
#     return current_user


def _setup_cors(p_app: FastAPI) -> None:
    p_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def _create_app() -> FastAPI:
    app_ = FastAPI(
        title=get_settings().PROJECT_NAME,
        openapi_url=urljoin(get_settings().API_V1_STR, "openapi.json"),
        version=get_settings().VERSION,
        docs_url="/swagger",
        swagger_ui_parameters={"oauth2RedirectUrl": f"{get_settings().API_V1_STR}/docs/oauth2-redirect"},
    )
    app_.include_router(api_router, prefix=get_settings().API_V1_STR)
    Base.metadata.create_all(bind=engine)
    return app_


app = _create_app()
_setup_cors(app)
