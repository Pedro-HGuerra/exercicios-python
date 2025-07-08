from datetime import datetime, date

def calcularIdade(dataNascimento):
    dataAtual = date.today()
    
    #Calcula quantos os dias totais
    idadeDias = (dataAtual - dataNascimento).days

    #Calcula quantos anos bissextos ocorreram
    anosBissextos = 0
    ano = int(dataNascimento.year)
    while ano < int(dataAtual.year):
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            anosBissextos += 1
        ano += 1
    print(anosBissextos)

    #Calcula os anos
    anos = idadeDias // 365

    #Calcula meses
    diasRestantes = idadeDias % 365
    print(diasRestantes)

    

    meses = diasRestantes // 30

    dias = diasRestantes % 30   

    print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")

strDataNascimento = input(f"Informe sua data de nascimento (DD/MM/YYYY): ")

dataNascimento = datetime.strptime(strDataNascimento, '%d/%m/%Y').date()

calcularIdade(dataNascimento)