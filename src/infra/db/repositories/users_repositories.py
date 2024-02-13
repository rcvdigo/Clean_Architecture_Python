from src.infra.db.settings.connection import DbConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity


class UsersRepository:
    
    @classmethod # Nos parametros os ": type-hitss" é como se fosse um tipo de comentário, ex docstring
    def insert_user(
        cls,
        first_name: str,
        last_name: str,
        age: int
    ) -> None: # A conveção diz que classes de métodos ao invés de self usasse cls

        with DbConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as ex:
                database.session.rollback()
                raise ex
            
    @classmethod
    def select_user(
        cls,
        first_name: str
    ) -> any:
        
        with DbConnectionHandler() as database:
            try:
                users = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as ex:
                database.session.rollback()
                raise ex
