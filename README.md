Projeto LFC - Grupo 19
Integrantes
André Vinícius Zicka Schmidt — GitHub: andrevzs
Gabriel Fischer Domakoski — GitHub: fochu3013
Descrição

Este projeto implementa um sistema para:

Análise léxica de expressões em notação polonesa reversa (RPN)
Execução das expressões com suporte a operações matemáticas e comandos especiais
Geração de código Assembly ARMv7 compatível com o CPULATOR (DEC1-SOC)

O sistema é dividido em três partes principais:

Lexer → transforma o texto em tokens
Executor → interpreta as expressões e gerencia memória/resultados
Assembler → gera o código Assembly correspondente
Como executar

No terminal:

python main.py teste1.txt

Você pode usar também:

python main.py teste2.txt
python main.py teste3.txt
Arquivos de entrada

Os arquivos de teste (teste1.txt, teste2.txt, teste3.txt) contêm expressões no formato RPN, por exemplo:

(3.14 2.0 +)
(5 RES)
(10.5 CONTADOR)
(MEM)
((2 3 +) (4 5 *) /)
Saídas geradas

Após executar o programa, são gerados:

tokens.txt → tokens identificados pelo analisador léxico
output.asm → código Assembly ARMv7 equivalente
Operadores suportados
Aritméticos
+ → soma
- → subtração
* → multiplicação
/ → divisão real
// → divisão inteira
% → resto
^ → potência
Comandos especiais
(N RES) → acessa o resultado da linha N
(VALOR MEM) → armazena valor em memória
(MEM) → recupera valor armazenado
Observações importantes
O Assembly gerado é compatível com o ambiente CPULATOR ARMv7 (DEC1-SOC)
As operações // e % foram implementadas manualmente (sem uso de SDIV), garantindo compatibilidade com o processador
Cada linha gera um resultado armazenado em memória (RES_LINHA_X)
Estrutura do projeto
lexer.py       → análise léxica
executor.py    → execução das expressões
assembler.py   → geração de Assembly
main.py        → controle do fluxo do programa

teste1.txt
teste2.txt
teste3.txt

tokens.txt
output.asm
Como testar no CPULATOR
Execute o programa para gerar o output.asm
Copie o conteúdo do arquivo
Cole no CPULATOR (ARMv7 DEC1-SOC)
Compile e execute
Estado do projeto

✔ Analisador léxico funcional
✔ Execução de expressões RPN
✔ Suporte a memória e histórico de resultados
✔ Geração de Assembly completa
✔ Compatível com CPUlator
