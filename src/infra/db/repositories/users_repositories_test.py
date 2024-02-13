import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DbConnectionHandler
from .users_repositories import UsersRepository


# Instanciando conexão com o banco de dados
db_connection_handler = DbConnectionHandler()

# Conexao realizada
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    # Dados a serem inseridos:
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 34

    # Instanciando a tabela a ser inseridos os dados:
    users_repository = UsersRepository()

    # Efetivando inserção de dados a tabela users na entidade UsersRepository
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    # Criando uma consulta a ser realizada após inserção de dados
    query = f'''
        SELECT * FROM users
        WHERE first_name = '{mocked_first_name}'
        AND last_name = '{mocked_last_name}'
        AND age = {mocked_age}
    '''

    # Instanciando a consulta realizada
    response = connection.execute(text(query))
    
    # Fazendo a consulta da primeira linha
    registry = response.fetchone()

    # Verificando se houve a inserção dos dados de forma conforme a esperada
    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    # Deletando o dado que foi inserido com sucesso para não superpopular a tabela
    # Pois se trata de um teste
    connection.execute(text(
        f'''
        DELETE FROM users
        WHERE id = {registry.id}
        '''
        ))
    
    # Comitando a tabela após deleção do dado.
    connection.commit()

    # Debugando no terminal a consulta realizada
    print(f"\n\n{registry}\n\n")


# @pytest.mark.skip(reason="Sensive test")
def test_select_user():

    # Dados a consultados:
    mocked_first_name = 'first_2'
    mocked_last_name = 'last_2'
    mocked_age = 34

    query = f'''
        INSERT INTO users (first_name, last_name, age)
        VALUES ('{mocked_first_name}', '{mocked_last_name}', '{mocked_age}')
    '''

    connection.execute(text(query))
    connection.commit()

    # Instanciando a tabela a ser inseridos os dados:
    users_repository = UsersRepository()

    response = users_repository.select_user(mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    connection.execute(text(
        f'''
        DELETE FROM users WHERE id = {response[0].id}
        '''
        ))
    
    connection.commit()

    print(f"\n\n{response}\n")
