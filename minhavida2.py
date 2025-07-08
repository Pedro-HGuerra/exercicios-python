import datetime
from dateutil.relativedelta import relativedelta

def calcularIdade(dataNascimento):
    dataAtual = datetime.date.today()
    idade = relativedelta(dataAtual, dataNascimento)
    print(f"Você possui {idade.years} anos, {idade.months} meses e {idade.days} dias!!!!!!")

dataNascimento = datetime.date(2003, 12, 24)

calcularIdade(dataNascimento)