def abrirArquivo(arquivo):
    texto =  open('{}'.format(arquivo), 'r').read()
    return texto