import sqlite3
from pathlib import Path
import os.path
from datetime import datetime


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
dia = datetime.now()
cursor.execute(
	f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
	'Id INTEGER PRIMARY KEY AUTOINCREMENT,'
	'Nome TEXT,'
	'Deposito DOUBLE,'
    'Saque DOUBLE,'
    'Saldo DOUBLE,'
	'Data TEXT,' 
	'Contas DOUBLE'
	')'

)
connection.commit()

print(' Informe os valores  ')
nome = input('Nome do responsável: ')

cursor.execute(f"SELECT Saldo FROM {TABLE_NAME} WHERE Nome = ? ORDER BY Id DESC LIMIT 1", (nome,))

resultado = cursor.fetchone()	

if resultado:
    saldo = resultado[0]
    print(f"Saldo anterior: R$ {saldo:.2f}")
else:
    saldo = 0.0
    print("Nenhum saldo anterior encontrado. Iniciando com R$ 0.00")
			   

deposito = float (input('Depósito R$: '))
saque = float (input('Saque R$: '))
contas = float (input('Contas a pagar: '))



connection.commit()

if deposito > 0:
	saldo += deposito
if saque > saldo:
	print("Saldo insuficiente")
else:
	saldo = saldo - saque

if contas > saldo:
	print("Saldo insuficiente para concluir a transação")
else:	
	saldo = saldo - contas

connection.commit()

data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sql = (
	f'INSERT INTO {TABLE_NAME} '
	'(Nome, Deposito, Saque, Saldo, Contas, Data) '
	'VALUES ( ?, ?, ?, ?, ?,?)'
)
cursor.execute(sql, ( nome, deposito, saque, saldo, contas,data_atual))
connection.commit()

print(f"Saldo atual: R$ {saldo:.2f}")

cursor.close()
connection.close()