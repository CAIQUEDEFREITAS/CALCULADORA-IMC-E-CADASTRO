def calculaimc():
    print('---=== Calculadora IMC ===---')
    altura = float(input('Digite a sua altura cm: '))
    peso = float(input('Digite o seu peso em kg: '))

    imc = peso / (altura/100)**2

    if imc < 18.5:
        resultado = 'Magreza'
    elif 18.5 <= imc <= 24.9:
        resultado = 'Normal'
    elif 25.0 <= imc <= 29.9:
        resultado = 'Sobrepeso'
    elif 30.0 <= imc <= 39.9:
        resultado = 'Obeso'
    else:
        resultado = 'Obesidade grave'

    print(resultado)
    return resultado
