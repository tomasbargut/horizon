import pytest

from horizon import Query, Table, Field

@pytest.fixture()
def table():
    return Table("A")

@pytest.fixture()
def fields_example():
    return Field("a"), Field("b")

@pytest.fixture()
def table_fields(fields_example):
    return Table("A", *fields_example)

def test_table():
    name = "sarasa"
    table = Table(name)
    assert str(table) == table.name
    assert str(table) == name

def test_field():
    name = "sarasa"
    field = Field(name)
    assert str(field) == field.name
    assert str(field) == name

class TestSelect():
    def test_select(self, table):
        query = Query(table)
        hard_query = """SELECT * FROM {0}""".format(str(table)).strip()
        parsed_query = str(query.select()).strip()
        assert  parsed_query == hard_query

    def test_select_fields(self, table_fields):
        query = Query(table_fields)
        hard_query = "SELECT {0} FROM {1}".format(
            ",".join(
                [str(field) for field in table_fields.fields]
            ),
            table_fields, 
        )
        parsed_query = str(query.select())
        assert hard_query == parsed_query

    def test_select_query(self, table, fields_example):
        query = Query(table, *fields_example)
        hard_query = "SELECT {0} FROM {1}".format(
            ",".join(
                [str(field) for field in fields_example]
            ),
            table, 
        )
        parsed_query = str(query.select())
        assert hard_query == parsed_query
    