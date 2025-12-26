from fastapi import FastAPI, Path, Query, Depends
from typing import Optional, List
from uuid import UUID

from app.dependencies import common_query_params

app = FastAPI(
    title="Advanced FastAPI Parameters",
    description="Examples of advanced path and query parameter handling",
    version="1.0.0"
)
