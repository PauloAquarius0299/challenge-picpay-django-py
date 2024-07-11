from django.core.exceptions import ValidationError 

def validate_cpf(value):
    cpf = ''.join([char for char in value if char.isdigit()])
    
    if len(cpf) != 11:
        raise ValidationError('CPF inválido')
    
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')
    
    def calcular_digito(cpf, multiplicadores):
        soma = sum(
            int(cpf[i]) * multiplicadores[i]
            for i in range(len(multiplicadores))
        )
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    multiplicadores_primeiro = list(range(10, 1, -1))
    primeiro_digito = calcular_digito(cpf, multiplicadores_primeiro)
    
    multiplicadores_segundo = list(range(11, 1, -1))
    segundo_digito = calcular_digito(cpf, multiplicadores_segundo)
    
    if not (cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito)):
        raise ValidationError('CPF inválido')
    