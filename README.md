🏭 Sistema de Automação Digital: Gestão de Qualidade Industrial
Este projeto consiste num protótipo de um sistema lógico desenvolvido em Python para o controlo de produção e inspeção de qualidade numa linha de montagem industrial. A solução automatiza a verificação de conformidade de peças, gere o armazenamento em caixas e gera relatórios estatísticos.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.11+

Base de Dados: SQLite (Persistência local)

Paradigma: Programação Estruturada e Modular

📖 Manual de Utilização
Este manual descreve o passo a passo para operar o sistema e as regras de negócio aplicadas.

1. Preparação e Execução
Certifica-te de que tens o Python instalado no teu sistema.

Faz o download do ficheiro main.py.

Abre o terminal na pasta do ficheiro e executa o comando:

Bash
python main.py
Nota: O sistema criará automaticamente o ficheiro producao_industrial.db na primeira execução.

2. Regras de Aprovação (Critérios de Qualidade)
Para que uma peça seja classificada como APROVADA, ela deve cumprir simultaneamente os seguintes requisitos:

Peso: Entre 95g e 105g (inclusive).

Cor: Apenas "Azul" ou "Verde" (o sistema ignora maiúsculas/minúsculas).

Comprimento: Entre 10cm e 20cm (inclusive).

Se qualquer um destes critérios falhar, a peça é registada como REPROVADA e o motivo da falha é armazenado.

3. Operação do Menu
Ao iniciar o programa, terás as seguintes opções:

Opção 1 - Cadastrar nova peça: Introduz os dados técnicos (Peso, Cor e Comprimento). O sistema gera um ID único automaticamente e informa imediatamente o status da peça.

Opção 2 - Listar peças cadastradas: Exibe todo o histórico de produção armazenado na base de dados, permitindo a rastreabilidade.

Opção 3 - Remover peça: Permite eliminar um registo específico através do número do ID.

Opção 4 - Gerar relatório final: Exibe o resumo da produção, incluindo o total de aprovadas/reprovadas e o status logístico das caixas.

4. Lógica de Armazenamento
O sistema gere automaticamente o fluxo de embalamento:

Cada caixa tem capacidade para 10 peças aprovadas.

Assim que a 10ª peça é aprovada, o sistema contabiliza uma caixa como "Fechada".

Peças reprovadas não ocupam espaço nas caixas de expedição.

📈 Estrutura de Dados
O projeto utiliza um dicionário para a manipulação temporária dos dados e uma tabela SQLite para a persistência. A escolha do SQLite garante que os dados de produção não sejam perdidos ao encerrar o software, simulando um ambiente industrial real.

✒️ Autor
Lucas Araújo Silva Simeão 
