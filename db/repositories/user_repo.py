from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.user import User

class UserRepository:

    async def create_user(
        self,
        session: AsyncSession,
        telegram_id: int,
        name: str = None,
        gender: str = None,
        character_class: str = None
    ):
        user = User(
            telegram_id=telegram_id,
            name=name,
            gender=gender,
            character_class=character_class
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user


    async def get_by_telegram_id(self, session: AsyncSession, telegram_id: int):
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()


    async def update_user(self, session: AsyncSession, user: User, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)

        await session.commit()
        await session.refresh(user)

        return user

    async def delete_user(self, session: AsyncSession, user: User):
        session.delete(user)
        await session.commit()