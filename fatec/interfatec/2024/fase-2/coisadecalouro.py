from sys import exit


def calcular_diferenca_dias(data_final, data_inicial, calendario_mapa):
    def converter_para_dia_do_ano(data, calendario):
        dia, mes = data
        total_dias = 0
        for i in range(1, mes):
            total_dias += calendario[i][1]
        total_dias += dia
        return total_dias

    dia_final_abs = converter_para_dia_do_ano(data_final, calendario_mapa)
    dia_inicial_abs = converter_para_dia_do_ano(data_inicial, calendario_mapa)

    return dia_final_abs - dia_inicial_abs


end_date = "quatorze de outubro"
tip = "1 dia"
start_date = "treze de outubro"

calendar = [
    "jan: 31",
    "fev: 28",
    "mar: 31",
    "abr: 30",
    "mai: 31",
    "jun: 30",
    "jul: 31",
    "ago: 31",
    "set: 30",
    "out: 31",
    "nov: 30",
    "dez: 31",
]

calendar_order = {
    "jan": 1,
    "fev": 2,
    "mar": 3,
    "abr": 4,
    "mai": 5,
    "jun": 6,
    "jul": 7,
    "ago": 8,
    "set": 9,
    "out": 10,
    "nov": 11,
    "dez": 12,
}

days = {
    "um": 1,
    "dois": 2,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20,
    "vinte e um": 21,
    "vinte e dois": 22,
    "vinte e tres": 23,
    "vinte e quatro": 24,
    "vinte e cinco": 25,
    "vinte e seis": 26,
    "vinte e sete": 27,
    "vinte e oito": 28,
    "vinte e nove": 29,
    "trinta": 30,
    "trinta e um": 31,
}

months = []

for month in calendar:
    month_name, day = month.split(":")
    months.append((int(calendar_order[month_name]), int(day)))

months.sort(key=lambda month: month[0])

end_date_parts = end_date.split()
end_date = (days[end_date_parts[0]], calendar_order[end_date_parts[2][:3]])

start_date_parts = start_date.split()
start_date = (days[start_date_parts[0]], calendar_order[start_date_parts[2][:3]])

start_month = months[start_date[1] - 1]

if (
    months[start_date[1] - 1][1] < start_date[0]
    or months[end_date[1] - 1][1] < end_date[0]
):
    print("data nao existe!")
    exit()

diffenrence = calcular_diferenca_dias(end_date, start_date, months)


integer, time = tip.split()
integer = int(integer)

estimation = 0
match time:
    case "dia" | "dias":
        estimation = integer
    case "semana" | "semanas":
        estimation = integer * 7
    case "mes" | "meses":
        estimation = integer * 30


if diffenrence == estimation:
    print("que caloura ousada!")
elif diffenrence < estimation:
    print("olha a reprovacao chegando!")
elif diffenrence > estimation:
    print("jovem consciente!")
else:
    print("esta de brincadeira?")
