from janela import *
from socket import *

cliente = socket(AF_INET, SOCK_STREAM)
host = gethostname()
porta = 1010

cliente.connect((host,porta))

