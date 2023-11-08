from sqlite3 import *
from typing import Any
from abc import *

class BuildQuery(ABC):
    @abstractmethod
    def createTable(table_name: str, keys: list) -> str:
        totalQuery = f"CREATE TABLE {table_name} (\n\t"
        totalQuery += ",\n\t".join(keys)
        totalQuery += "\n);"
        return totalQuery

    @abstractmethod
    def insertIntoTable(table_name:str, keys: list, values: list) -> str:
        totalKeys = ",".join(keys)
        totalValues = ",".join(values)
        totalQuery = f"INSERT INTO {table_name} ({totalKeys})\nVALUES "
        totalQuery += totalValues
        totalQuery += ";"
        return totalQuery

    @abstractmethod
    def viewContentInTable(table_name: str, keys: list=None, condition:str=None, orderBy:str=None) -> str:
        if keys is None: totalKeys="*"
        else: totalKeys = ",".join(keys)

        if condition is None: condition="1=1"

        if orderBy is None:
            return f"SELECT {totalKeys} FROM {table_name} WHERE {condition}"

        return f"SELECT {totalKeys} FROM {table_name} WHERE {condition} ORDER BY {orderBy}"

    @abstractmethod
    def updateDataInTable(table_name: str, keys: str, condition: str) -> str:
        totalQuery = f"UPDATE {table_name}\n"
        totalQuery += f"SET {keys}\n"
        totalQuery += f"WHERE {condition}"
        return totalQuery


class SQL:
    def __init__(self, database_path):
        self._path = database_path

        self._connection = connect(self._path)  # Database connection
        self._cursor = self._connection.cursor()  # Database cursor


    def executeCommands(self, commandToRun) -> list[Any]:
        try:
            self._commandResult = self._cursor.execute(commandToRun)
            self._connection.commit()
        except Exception as error_type:
            raise error_type
        else:
            return self._commandResult.fetchall()
