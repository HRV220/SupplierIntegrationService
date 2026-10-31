from app.core.config import settings
from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker, AsyncSession)
from typing import Annotated, AsyncGenerator
from fastapi import Depends

engine = create_async_engine(pool_pre_ping= True, url=settings.database_url)

async_session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
  async with async_session_factory() as session:
    try:
      yield session
      await session.commit()
    except Exception:
      await session.rollback()
      raise

SessionDep = Annotated[AsyncSession, Depends(get_db, scope="function")]