# Gerenciador de Tabela de Símbolos para Análise Semântica

Este projeto desenvolve um simulador de análise semântica voltado para a gestão de escopos aninhados e verificação de tipos (Type Checking). O sistema emprega uma pilha de tabelas hash para gerenciar o ciclo de vida, a visibilidade, a atribuição de valores e o sombreamento (shadowing) de variáveis ao longo da execução de um programa.

## Como Executar

O comando principal para rodar o projeto é:
python src/symbol_table.py

### Pré-requisitos para o comando funcionar:
* É necessário ter o Python 3 instalado no sistema.
* O terminal precisa estar aberto exatamente dentro da pasta raiz `compiladores`.

## Recursos Implementados (Robustez do Sistema)
* **Orientação a Objetos:** Armazenamento de identificadores utilizando uma classe dedicada `Simbolo` (guardando Nome, Tipo e Valor).
* **Verificação Estrita de Tipos (Type Checking):** O sistema impede e reporta erros de incompatibilidade (*Type Mismatch*) se você tentar atribuir um valor diferente do tipo declarado da variável.
* **Gerenciamento de Escopos:** Suporte completo para abertura e fechamento de blocos com liberação automática de memória e mascaramento de variáveis externas (*Shadowing*).


