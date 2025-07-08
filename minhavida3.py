from datetime import date

# Insira sua data de nascimento (ano, mês, dia)
nascimento = date(1990, 5, 20)

# Data atual
hoje = date.today()

# Calcula diferença total em dias
dias_totais = (hoje - nascimento).days

# Calcula anos, meses e dias com base na data
anos = hoje.year - nascimento.year

meses = hoje.month - nascimento.month
dias = hoje.day - nascimento.day

# Ajustes para meses e dias negativos
if dias < 0:
    meses -= 1
    dias += (date(hoje.year, hoje.month, 1) - date(hoje.year, hoje.month - 1, 1)).days

if meses < 0:
    anos -= 1
    meses += 12

print(f"Você viveu {anos} anos, {meses} meses e {dias} dias.")
