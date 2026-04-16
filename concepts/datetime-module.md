# Módulo de data Datetime (Datetime Module)

## O que é

O módulo `datetime` da biblioteca padrão do Python fornece classes para manipular datas e horários. Ele permite criar, formatar, comparar e validar objetos de data/hora de forma confiável, sem precisar lidar manualmente com casos como meses com 28, 30 ou 31 dias, ou anos bissextos.

A função `datetime.strptime()` (de *string parse time*) é especialmente útil para validação: ela tenta converter uma string em um objeto `datetime` segundo um formato especificado. Se a string não corresponder ao formato, lança uma exceção `ValueError` — o que permite detectar datas inválidas de forma elegante.

## Como é usado neste projeto

A função `validar_data()` em `estoque.py` usa `datetime.strptime()` para garantir que o usuário forneça uma data no formato `dd/mm/aaaa`. O formato `'%d/%m/%Y'` instrui o parser a esperar dia com dois dígitos, mês com dois dígitos e ano com quatro dígitos, separados por barras.

Se a data digitada não existir (como `30/02/2025`) ou estiver em formato errado, `strptime` lança `ValueError`, que é capturado pelo `except` e resulta em uma nova tentativa.

## Exemplo do projeto

```python
from datetime import datetime

def validar_data():
    """Solicita e valida uma data no formato dd/mm/aaaa"""
    data = input('\nDigite a data da movimentação (ou digite 0 para cancelar): ')
    
    while True:
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return data
        except ValueError:
            print('Data inválida. Use o formato dd/mm/aaaa\n')
            data = input('Digite a data da movimentação: ')
```

## Recursos para aprofundamento

- [Python Docs — datetime](https://docs.python.org/pt-br/3/library/datetime.html) — referência completa do módulo
- [strftime.org](https://strftime.org/) — referência visual para os códigos de formato de data
