import pytest
from src.models.connection.connection_handler import DbConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DbConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "ola": "mundo" }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{ "elem1": "aqui" }, { "elem2": "aqui2" }, { "elem3": "aqui3" }]
    orders_repository.insert_list_of_documents(my_doc)