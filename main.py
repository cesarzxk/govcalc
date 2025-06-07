from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def calc_inss(salario):
    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14)
    ]

    teto_inss = 908.85  # Teto de contribuição para 2025
    inss_total = 0.0
    faixa_anterior = 0.0

    for teto, aliquota in faixas:
        if salario > teto:
            faixa_base = teto - faixa_anterior
        else:
            faixa_base = salario - faixa_anterior

        if faixa_base > 0:
            inss_total += faixa_base * aliquota

        faixa_anterior = teto

        if salario <= teto:
            break

    return min(inss_total, teto_inss)



def calc_irrf(valor, inss, aliquota, deducao):
    return (valor - inss) * aliquota - deducao

@app.route('/calcular-salario', methods=['POST'])
def calcular_salario():
    data = request.get_json()

    salario = data.get('salario', 0)
    aliquota_irpf = data.get('aliquota_irpf', 0.225)
    irpf_deducao = data.get('irpf_deducao', 675.49)
    beneficios = data.get('beneficios', 0)
    descontos = data.get('descontos', 0)

    inss = calc_inss(salario)
    irpf = calc_irrf(salario, inss, aliquota_irpf, irpf_deducao)
    liquido = salario - inss - irpf

    salario_ferias = salario * 1.33
    ferias_inss = calc_inss(salario_ferias)
    ferias_irpf = calc_irrf(salario_ferias, ferias_inss, aliquota_irpf, irpf_deducao)
    ferias_liquido = salario_ferias - ferias_inss - ferias_irpf

    fgts = salario * 0.08
    decimo_terceiro = liquido

    total_mensal = (
        liquido +
        (ferias_liquido / 12) +
        (decimo_terceiro / 12) +
        fgts +
        beneficios -
        descontos
    )

    return jsonify({
        "inss": round(inss, 2),
        "irpf": round(irpf, 2),
        "salario_liquido": round(liquido, 2),
        "ferias_liquido": round(ferias_liquido, 2),
        "fgts": round(fgts, 2),
        "decimo_terceiro": round(decimo_terceiro, 2),
        "total_mensal": round(total_mensal, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
