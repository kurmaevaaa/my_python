salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

i = months
money_capital = 0
while i > 0:
    money_capital += spend - salary
    spend *= increase +1
    i -= 1
for j in range(20000):
    if 0 < j-money_capital < 1:
        money_capital = j
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
