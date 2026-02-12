from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI(
    default_response_class=JSONResponse
)