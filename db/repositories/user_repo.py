def create_user(
    self,
    session: Session,
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
    session.commit()
    session.refresh(user)

    return user


def get_by_telegram_id(self, session: Session, telegram_id: int):
    return session.query(User).filter(User.telegram_id == telegram_id).first()


def update_user(self, session: Session, user: User, **kwargs):
    for key, value in kwargs.items():
        setattr(user, key, value)

    session.commit()
    session.refresh(user)

    return user

def delete_user(self, session: Session, user: User):
    session.delete(user)
    session.commit()