import os # Verifica o sistema e limpa a tela
# os.name =='nt' identifica se o sistema é Windows, executando o comando o comando 'cls' para limpar a tela. 
# Caso contrário (else), para sistemas Linux ou Mac (baseados em Unix), o comando 'clear' é utilizado.
# os.name == 'nt' significa que o sistema operacional é Windows, enquanto 'posix' indica Linux ou Mac.
# os.name retorna 'nt' para Windows e 'posix' para Linux/Mac
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Linux/Mac
    os.system('clear')

# Início do programa:
# Programa utilizando estruturas de decisão match:case.
print("#*"* 33)
print("Menu de suporte técnico e seus respectivos status de atendimento.!")
print("#*" * 33)

# Entrada de dados pelo usuário. 
# O usuário deve informar o status do atendimento técnico.
# Para isso, ele deve digitar uma das seguintes opções: p (Pendente), e (Enviado) ou c (Cancelado).
status = input("Digite o status do atendimento técnico (p, e ou c): ").strip().lower()
# .strip() remove espaços em branco no início e no final da string, enquanto .lower() converte a string para letras minúsculas.

# Processamento e saída de dados
# O programa utiliza a estrutura de decisão match:case para verificar o status do atendimento técnico informado pelo usuário.
# Dependendo do status informado, o programa exibirá uma mensagem correspondente.
match status: # A estrutura de decisão match, compara o valor da variável status com os valores especificados nos casos (case).
    case "p":
        print("Seu pedido está Pendente e em processamento.")
    case "e":
        print("Seu pedido já foi Enviado! Verifique seu e-mail")
    case "c":
        print("Seu pedido foi Cancelado. Entre em contato com o RH.")
    case _:
        print("Opção inválida. Tente novamente.")