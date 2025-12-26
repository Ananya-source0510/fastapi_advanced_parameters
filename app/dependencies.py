from fastapi import Query
from typing import Optional

def common_query_params(
    q: Optional[str] = Query(None, min_length=3),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return {"q": q, "limit": limit, "offset": offset}
