import csv

input_file_path = 'alunos_ifrn.csv'
output_campus_file_path = 'alunos_ifrn_campus.csv'
output_ano_file_path = 'alunos_ifrn_ano.csv'
output_campus_curso_file_path = 'alunos_ifrn_campus_curso.csv'

with open(input_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    alunos = list(reader)


campus_dict = {}
total_alunos = 0

for aluno in alunos:
    campus = aluno['campus']
    campus_dict[campus] = campus_dict.get(campus, 0) + 1
    total_alunos += 1

campus_list = []
for campus, qtd in campus_dict.items():
    percentual = round((qtd / total_alunos) * 100, 2)
    campus_list.append([campus, qtd, percentual])

with open(output_campus_file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for campus_data in campus_list:
        writer.writerow([str(item).replace(';', ';;') for item in campus_data])

ano_dict = {}

for aluno in alunos:
    ano = aluno['matricula'][:4]  
    ano_dict[ano] = ano_dict.get(ano, 0) + 1

ano_list = [[ano, qtd] for ano, qtd in ano_dict.items()]

with open(output_ano_file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for ano_data in ano_list:
        writer.writerow([str(item).replace(';', ';;') for item in ano_data])

campus_escolhido = 'CNAT'  

curso_dict = {}

for aluno in alunos:
    if aluno['campus'] == campus_escolhido:
        curso = aluno['curso']
        curso_dict[curso] = curso_dict.get(curso, 0) + 1

curso_list = [[curso, qtd] for curso, qtd in curso_dict.items()]

with open(output_campus_curso_file_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for curso_data in curso_list:
        writer.writerow([str(item).replace(';', ';;') for item in curso_data])

print("Arquivos gerados com sucesso.")
