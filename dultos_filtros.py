def retirawww(nome):
    return  nome.replace("www.","https//")
def retirabarras(nome):
    return nome.replace('/',".")
def retiraPontocom(nome):
    return nome.replace(".com","")
def urlfinanl(url):
    url = retirawww(url)
    url = retirabarras(url)
    url = retiraPontocom(url)
    return url

url = input('coloque aqui sua url')

print(urlfinanl(url))

