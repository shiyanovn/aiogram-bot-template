from logging.config import fileConfig
from pathlib import Path
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from app.data.db import DeclarativeBase
from app.data.config import get_settings
from dotenv import load_dotenv
import asyncio
import os

env_path = Path(__file__).parents[2] / '.env'
load_dotenv(dotenv_path=env_path)

settings = get_settings()
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = DeclarativeBase.metadata

def get_database_url():
    return (
        f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
        f"postgres-aiogram:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    )

def run_migrations_offline():
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    connectable = create_async_engine(get_database_url())
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())