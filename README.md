# Calculadora de Salário - API Flask + Interface Web

Este projeto consiste em uma API Flask que calcula salário líquido, INSS, IRPF, férias, FGTS e décimo terceiro, e uma interface web simples para enviar dados e visualizar o resultado.

---

### Funcionalidades

- Cálculo de INSS baseado em faixas progressivas.
- Cálculo de IRPF com deduções.
- Cálculo de salário líquido, férias líquidas, FGTS, décimo terceiro e total mensal.
- Interface web para envio dos dados e exibição dos resultados.
- Permite informar salário, alíquota IRPF, deduções, benefícios e descontos.

---

### Como usar

Pré-requisitos

- Python 3.7+
- pip instalado

Instalação

1. Clone o repositório (ou baixe os arquivos).

2. Instale as dependências:
```
pip install -r requirements.txt

```

Rodar a API

Execute o arquivo app.py:

```
python app.py
```

A API vai rodar em http://localhost:5000

Abrir a interface

Abra o arquivo index.html no seu navegador (Google Chrome, Firefox, etc).

Preencha os campos e clique em Calcular para ver os resultados.

A interface faz requisição POST para a API local.

---

Ajustes importantes

- A API permite chamadas CORS para funcionar com a interface local.
- A alíquota INSS é calculada automaticamente conforme faixas, não precisa ser enviada pela interface.

---

Estrutura dos arquivos

- app.py — servidor Flask com as rotas e lógica.
- index.html — interface web para interação.
- README.md — este arquivo.
