from typing import (
    List, TypeVar, Any,Optional, Tuple
)
from horizon.fields import (
    Field, ComodinField
)



class Table:
    name: str
    fields: Tuple[Field,...]

    def __init__(self, name: str, *fields: Field):
        self.name = name
        self.fields = fields

    def __str__(self):
        return self.name

class Query:
    fields: Tuple[Field,...]

    def __init__(self, table: Table, *fields: Field):
        self.table = table
        if fields:
            self.fields = fields 
        elif table.fields:
            self.fields = table.fields
        else:
            self.fields = ComodinField,

    def select(self, *fields: Field):
        if not fields:
            fields = self.fields

        joined_fields = ",".join(str(field) for field in fields)

        self._query = """SELECT {fields} FROM {table}""".format(
            fields=joined_fields, table=str(self.table)
        )
        return self

    def __str__(self):
        return self._query
