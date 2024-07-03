import mysql.connector as msql

'''Isso daqui vai mudar quando o banco estiver no local correto'''

class DataBase:
    def __init__(self) -> None:
        self.db = msql.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='arvometro'
        )
        self.cursor = self.db.cursor()

    def test_connection(self) -> None:
        print(self.db)

    def insert(self, table: str, data: tuple):
        if table == 'donatario':
            query = 'insert into donatario (nome_completo, data_nascimento, bairro, telefone) values (%s, %s, %s, %s)'
        elif table == 'doacao':
            query = 'insert into doacao (data_doacao, foi_evento, evento, id_muda, id_donatario, qtd_doadas) values (%s, %s, %s, %s, %s, %s)'
        self.cursor.execute(query, data)
        self.db.commit()

    def select(self, table_name: str):
        query = f'select * from {table_name}'
        self.cursor.execute(query)
        return [elem for elem in self.cursor.fetchall()]

    def update(self, table_name: str, column: str, new_value, id):
        query = f'update {table_name} set {column} = {new_value} where id_{table_name} = {id}'
        self.cursor.execute(query)
        self.db.commit()
