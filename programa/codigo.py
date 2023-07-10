print('Validador de CPF')

while True:
    print("Digite seu CPF com os '.' e o '-' ")
    cpf_enviado_usuario = input('CPF: ')

    if len(cpf_enviado_usuario) != 14 or '-' not in cpf_enviado_usuario or '.' not in cpf_enviado_usuario:
         print('CPF Incorreto!')
         print('Tente de novo!')
         continue
 
    # Tratando o CPF
    cpf_formatado = cpf_enviado_usuario.replace('.', '').replace('-', '')
    entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
    
    if entrada_e_sequencial:
        print('Você enviou dados sequenciais.')
        print('Tente de novo!')
        continue
    # Pegando os noves primeiros digitos
    nove_digitos = cpf_formatado[:9]

    # Multiplicando e somando os 9 primeiros dígitos do CPF
    contador_regresivo_1 = 10
    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regresivo_1
        contador_regresivo_1 -= 1

    # Calculando o Primeiro dígito
    digito_1 = (resultado_1 * 10) % 11
    
    # Validando o resultado
    digito_1 = digito_1 if digito_1 <= 9 else 0

    """-------- Calculo do segundo Digito ----------"""
    
    # Pegando os dez primeiros dígitos
    dez_digitos = cpf_formatado[:9] + str(digito_1)

    # Multiplicando e somando os dez primeiros dígitos do CPF
    contador_regresivo_2 = 11
    resultado_2 = 0
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regresivo_2
        contador_regresivo_2 -= 1

    # Calculando o Segundo dígito
    digito_2 = (resultado_2 * 10) % 11

    # Validando o segundo dígito
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Validação de CPF inteiro

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    
    if cpf_gerado_pelo_calculo == cpf_formatado:
        print('Seu CPF é valido!')
    else:
        print('Seu CPF é Inválido!')
    break