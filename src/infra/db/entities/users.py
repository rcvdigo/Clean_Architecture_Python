from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer


from src.infra.db.settings.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    first_name = Column(
        String(255),
        nullable=False
    )
    last_name = Column(
        String(255),
        nullable=False
    )
    age = Column(
        Integer,
        nullable=False
    )

    def __repr__(self):
        return f"""
        Users [
            id={self.id} 
            first_name={self.first_name}
            last_name={self.last_name}
            age={self.age}
        ]
        """
