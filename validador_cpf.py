def verificar_cpf(cpf):
    # Remover os pontos e os traços
    valores_cpf = formatar_cpf(cpf)
        
    # Verificar se o CPF é válido (11 dígitos e não são todos iguais)
    if not cpf_eh_valido(valores_cpf):
        return "CPF inválido"
    
    # Pegamos os verificadores
    digitos_verificadores = [int(valores_cpf[9]), int(valores_cpf[10])]
    
    # Cálculo do primeiro verificador
    peso = 10
    soma_valores = soma_com_pesos(valores_cpf, peso)
    resto_divisao = soma_valores % 11
    verificador_1 = define_verificador(resto_divisao)
    
    if verificador_1 != int(digitos_verificadores[0]):
        return "CPF inválido. O primeiro verificador é errado"
    
    # Cálculo do segundo verificador
    peso = 11
    nova_soma = soma_com_pesos(valores_cpf, peso) + verificador_1 * 2
    
    resto_divisao = nova_soma % 11
    verificador_2 = define_verificador(resto_divisao)
    
    if verificador_2 != int(digitos_verificadores[1]):
        return "CPF inválido. O segundo verificador é errado"
    
    return "CPF válido"

# Define o valor do verificador
def define_verificador(valor):
    if valor < 2:
        return 0
    else:
        return 11 - valor

# Realiza a soma dos itens usando o peso
def soma_com_pesos(valores, peso):
    soma = 0
    for i in range(9):
        soma += int(valores[i]) * peso
        peso -= 1
    
    return soma

# Verifica se é válido o CPF
def cpf_eh_valido(cpf):
    if todos_digitos_iguais(cpf) or len(cpf) != 11:
        return False
    
    return True

# Verifica se todos os dígitos são iguais
def todos_digitos_iguais(valores_cpf):
    return len(set(valores_cpf)) == 1


# Verifica se o cpf está todo numérico ou com separadores
def formatar_cpf(cpf): 
    if("." in cpf or "-" in cpf):
        return cpf.replace(".", "").replace("-", "")
    
    return cpf