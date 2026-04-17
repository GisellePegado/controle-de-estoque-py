<div align="center">

# Controle de Estoque

Sistema de controle de estoque via terminal, com registro de movimentações e histórico de auditoria.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-3776AB.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

</div>

---

## 📋 Sobre

Sistema de gestão de estoque implementado em Python puro, executado no terminal (CLI). Permite registrar entradas e saídas de produtos, manter um histórico completo de movimentações com responsável e data, e consultar o estado atual do estoque a qualquer momento.

Desenvolvido como projeto prático para a disciplina de Engenharia de Software, o sistema demonstra conceitos fundamentais de programação como modularização com funções, validação de entrada, estruturas de dados e gerenciamento de estado em memória.

## 🚀 Tecnologias

- **Python 3.6+** — linguagem principal do projeto
- **datetime** (biblioteca padrão) — validação e parsing de datas no formato `dd/mm/aaaa`

## 📁 Estrutura do projeto

```
controle-de-estoque-py/
├── estoque.py          ← código-fonte principal do sistema
├── docs/
│   ├── README.md                                    ← índice geral com links agrupados por categoria
│   ├── 1-requirements/
│   │   ├── 1-user-stories.md                        ← HU-01 e HU-02 com critérios de aceitação
│   │   ├── 2-funcional.md                           ← requisitos funcionais (RFs)
│   │   └── 3-non-funcional.md                       ← requisitos não funcionais (RNFs)
│   ├── 2-planning/
│   │   └── kanban.md                                ← Sprint board e backlog priorizado
├── concepts/           ← documentação dos conceitos usados no projeto
│   ├── README.md
│   ├── python-dictionaries.md
│   ├── modularization-functions.md
│   ├── input-validation.md
│   ├── datetime-module.md
│   ├── in-memory-state.md
│   ├── guard-clause.md
│   ├── cli-menu-pattern.md
│   ├── event-log.md
│   ├── fstring-formatting.md
│   └── entry-point-guard.md
├── README.md
└── LICENSE
```

## ⚙️ Como executar

```bash
# Clone o repositório
git clone https://github.com/GisellePegado/controle-de-estoque-py.git
cd controle-de-estoque-py

# Execute o sistema (Python 3.6+)
python estoque.py
```

Não há dependências externas — apenas a biblioteca padrão do Python.

## 🧭 Fluxo de Desenvolvimento

```
História de Usuário
        ↓
Requisitos Funcionais e Não Funcionais
        ↓
Planejamento com Quadro Scrum (Kanban)
        ↓
Implementação em Python
        ↓
Testes e Validação
```

Este fluxo reflete as práticas recomendadas pela Engenharia de Software para garantir que o sistema entregue valor real ao usuário final com qualidade e rastreabilidade.

## 🖥️ Funcionalidades

| Opção               | Descrição                                                    |
| ------------------- | ------------------------------------------------------------ |
| `1` — Movimentação  | Registra entrada ou saída de produto, com data e responsável |
| `2` — Histórico     | Lista todas as movimentações da sessão em formato de tabela  |
| `3` — Estoque atual | Exibe a quantidade disponível de cada produto                |
| `0` — Sair          | Encerra o sistema                                            |

## 📖 Documentação

A pasta [`docs/`](docs/) contém a documentação de engenharia de software do projeto, derivada das histórias de usuário e requisitos da disciplina:

| Documento                                                                         | Descrição                                                              |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [Histórias de Usuário](docs/1-requirements/1-user-stories.md)                     | HU-01 (entrada) e HU-02 (saída) com critérios de aceitação             |
| [Requisitos Funcionais](docs/1-requirements/2-functional.md)                      | RF01–RF06 com status de implementação                                  |
| [Requisitos Funcionais e Não Funcionais](docs/1-requirements/3-non-functional.md) | RNF01–RNF06 com status de implementação                                |
| [Quadro Kanban](docs/2-planning/kanban.md)                                        | 10 tarefas concluídas e 2 em progresso e 4 no backlog no formato Scrum |

## 📚 Conceitos explorados

Este projeto utiliza os seguintes conceitos de programação e arquitetura, documentados na pasta [`concepts/`](concepts/):

| Conceito                                                          | Descrição resumida                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Dicionários Python](concepts/python-dictionaries.md)             | Estrutura principal para armazenar produtos com acesso direto por código |
| [Modularização com Funções](concepts/modularization-functions.md) | Cada operação encapsulada em uma função de responsabilidade única        |
| [Validação de Entrada](concepts/input-validation.md)              | Loop `while` + `try/except` para garantir dados corretos do usuário      |
| [Módulo Datetime](concepts/datetime-module.md)                    | Parsing e validação de datas com `strptime`                              |
| [Estado em Memória](concepts/in-memory-state.md)                  | Dados mantidos em variáveis globais durante a execução                   |
| [Cláusula de Guarda](concepts/guard-clause.md)                    | Retorno antecipado com `None` para tratar cancelamentos                  |
| [Menu CLI](concepts/cli-menu-pattern.md)                          | Loop principal com menu de opções no terminal                            |
| [Registro de Eventos](concepts/event-log.md)                      | Histórico imutável de todas as movimentações realizadas                  |
| [Formatação com f-strings](concepts/fstring-formatting.md)        | Tabelas alinhadas no terminal com especificadores de formato             |
| [Ponto de Entrada \_\_name\_\_](concepts/entry-point-guard.md)    | Guarda `if __name__ == '__main__':` para definir o ponto de entrada      |

> Os arquivos de conceito contêm explicações detalhadas, exemplos extraídos do código e links para aprofundamento.

## 🤝 Contribuindo

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
