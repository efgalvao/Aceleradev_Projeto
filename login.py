import jwt
from time import time # para geracao da timestamp

secret = 'aceleradev'

user_id = efg

payload = {
  'uid': user_id,
  'exp': int(time()) + 3600 # queremos que o token seja valido por uma hora
}

token = jwt.encode(payload, secret, algorithm='HS256')

# ------------------------------------------------------------------------

import jwt

secret = 'aceleradev'

meu_jwt = request['headers']['authorization'] # token

try:
  informacoes = jwt.decode(meu_jwt, secret, algorithm='HS256')
except ExpiredSignatureError:
  print('Seu token esta expirado!')
except DecodeError:
  print('Token invalido ou segredo incorreto!')
except:
  print('Outro erro!')
else:
  print(informacoes['uid']) # efg
