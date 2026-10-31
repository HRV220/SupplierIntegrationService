import pytest
from contextlib import asynccontextmanager
from app.db.session import get_db, engine
from sqlalchemy import text

db_context = asynccontextmanager(get_db)

@pytest.mark.asyncio
async def test_connection_db():
    try:
        async with db_context() as session:
            res = await session.execute(text("SELECT 1"))
            assert res.scalar_one() == 1
    finally:
        await engine.dispose()
