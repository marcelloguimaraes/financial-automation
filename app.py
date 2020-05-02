import csv
import datetime as dt

month = str(input("Digite o mês que deseja calcular os gastos: "))
salary = float(input("Digite o salário líquido do mês: "))

def read_expenses():
    with open('expenses.csv', newline='', encoding='utf-8') as cvs_file:
        reader = csv.DictReader(cvs_file)
        calculate_values(reader)

def calculate_values(reader):
    global total, remaining_amount, amount_to_invest
    total = round(sum(float(row['Amount']) for row in reader), 2)
    remaining_amount = round(salary - total, 2)
    amount_to_invest = round(remaining_amount * 0.15, 2)

def print_values():
    print("Total de gastos: {}".format(total))
    print("Dinheiro restante: {}".format(remaining_amount))
    print("Você deve guardar: {}".format(amount_to_invest))

def create_resume():
    file_name = "{}-{}.csv".format(month, dt.datetime.now().strftime('%Y'))
    with open(file_name, mode='w', newline='') as resume_file:
        resume_file = csv.writer(resume_file, delimiter=',')
        resume_file.writerow(['Total', 'Restante', 'Deve guardar'])
        resume_file.writerow([total, remaining_amount, amount_to_invest])

while salary <= 0:
    print("Salário não pode ser negativo")
    salary = float(input("Digite o salário líquido do mês: "))

read_expenses()
print_values()
create_resume()


        
