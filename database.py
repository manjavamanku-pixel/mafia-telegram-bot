import asyncpg
import os
from typing import Optional

pool: Optional[asyncpg.Pool] = None

async def get_pool() -> asyncpg.Pool:
    global pool
    if pool is None:
        db_url = os.environ.get("DATABASE_URL", "")
        pool = await asyncpg.create_pool(db_url, min_size=2, max_size=10)
    return pool

async def init_db() -> None:
    p = await get_pool()
    async with p.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                username TEXT DEFAULT '',
                first_name TEXT DEFAULT '',
                language TEXT DEFAULT 'uz',
                usz BIGINT DEFAULT 0,
                almaz INTEGER DEFAULT 0,
                games INTEGER DEFAULT 0,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0,
                balls INTEGER DEFAULT 0,
                created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)

async def get_user(user_id: int) -> Optional[dict]:
    p = await get_pool()
    async with p.acquire() as conn:
        row = await conn.fetchrow("SELECT * FROM users WHERE id=$1", user_id)
        return dict(row) if row else None

async def create_user(user_id: int, username: str, first_name: str, lang: str = "uz") -> dict:
    p = await get_pool()
    async with p.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO users(id, username, first_name, language) "
            "VALUES($1, $2, $3, $4) "
            "ON CONFLICT(id) DO UPDATE SET username=$2, first_name=$3 "
            "RETURNING *",
            user_id, username, first_name, lang
        )
        return dict(row)
