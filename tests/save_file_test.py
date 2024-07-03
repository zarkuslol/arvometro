import sys
sys.path.append('.')

from utils.data_file import DataFile

df = DataFile('data/users.csv')

#data = [2, 'Sebastião', '08/12/1971', 'Centro']
#df.save_data(data=data, index=['UsuarioID','Nome','Data de Nascimento','Bairro'])

print(df.load_data())
