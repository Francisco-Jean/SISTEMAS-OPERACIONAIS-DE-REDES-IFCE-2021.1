dados = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J',
'k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v',
'V','w','W','x','X','y','Y','z','Z','0','1','2','3','4','5','6','7','8','9')

def criptografar(texto):
    trocado = ''
    for x in texto:
        if dados.count(x):
            for y in dados:
                if x == y:
                    trocado += dados[(len(dados) -1) - dados.index(y)]
        else:
            trocado += x

    return trocado

def descriptografar(texto):
    destrocado = ''
    for x in texto:
        if dados.count(x):
            for y in dados:
                if x == y:
                    destrocado += dados[(len(dados) -1) - dados.index(y)]
        else:
            destrocado += x
            
    return destrocado

if __name__ == '__main__':
    main = criptografar('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789')
    print(main)
    main2 = descriptografar(main)
    print(main2)