import sqlite3

# --- CAMADA DE DADOS (SQLite) ---
def iniciar_db():
    conn = sqlite3.connect('producao_industrial.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pecas (
            id TEXT PRIMARY KEY,
            peso REAL,
            cor TEXT,
            comprimento REAL,
            status TEXT,
            motivo TEXT
        )
    ''')
    conn.commit()
    conn.close()

def salvar_peca(peca):
    conn = sqlite3.connect('producao_industrial.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pecas VALUES (?, ?, ?, ?, ?, ?)', 
                  (peca['id'], peca['peso'], peca['cor'], peca['comprimento'], peca['status'], peca.get('motivo', '')))
    conn.commit()
    conn.close()

def excluir_peca(id_peca):
    conn = sqlite3.connect('producao_industrial.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pecas WHERE id = ?', (id_peca,))
    conn.commit()
    conn.close()

# --- LÓGICA DO SISTEMA ---

def validar_peca(peso, cor, comprimento):
    erros = []
    if not (95 <= peso <= 105):
        erros.append(f"Peso fora (95g-105g)")
    if cor.lower() not in ['azul', 'verde']:
        erros.append("Cor inválida (Azul/Verde)")
    if not (10 <= comprimento <= 20):
        erros.append("Comprimento fora (10cm-20cm)")
    return erros

def cadastrar_peca():
    print("\n[ NOVO CADASTRO ]")
    try:
        id_p = input("ID da Peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor (Azul/Verde): ").strip().lower()
        comp = float(input("Comprimento (cm): "))

        lista_erros = validar_peca(peso, cor, comp)
        status = "Aprovada" if not lista_erros else "Reprovada"
        motivo = " | ".join(lista_erros)

        peca = {
            "id": id_p, "peso": peso, "cor": cor, 
            "comprimento": comp, "status": status, "motivo": motivo
        }

        salvar_peca(peca)
        if status == "Aprovada":
            print(f"✅ Peça {id_p} cadastrada e APROVADA!")
        else:
            print(f"❌ Peça {id_p} REPROVADA: {motivo}")
            
    except ValueError:
        print("⚠️ Erro: Insira apenas números para peso e comprimento.")

def listar_pecas():
    conn = sqlite3.connect('producao_industrial.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pecas')
    dados = cursor.fetchall()
    conn.close()

    print("\n--- LISTA GERAL DE PEÇAS ---")
    for d in dados:
        print(f"ID: {d[0]} | Status: {d[4]} | Detalhe: {d[5]}")

def gerar_relatorio():
    conn = sqlite3.connect('producao_industrial.db')
    cursor = conn.cursor()
    
    # Contagens
    cursor.execute("SELECT COUNT(*) FROM pecas WHERE status = 'Aprovada'")
    aprovadas = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM pecas WHERE status = 'Reprovada'")
    reprovadas = cursor.fetchone()[0]
    
    # Lógica de Caixas (10 peças por caixa)
    caixas_fechadas = aprovadas // 10
    pecas_na_caixa_atual = aprovadas % 10

    print("\n" + "="*35)
    print("      RELATÓRIO CONSOLIDADO")
    print("="*35)
    print(f"Total de Peças Aprovadas:   {aprovadas}")
    print(f"Total de Peças Reprovadas:  {reprovadas}")
    print(f"Caixas Fechadas (Full):     {caixas_fechadas}")
    print(f"Peças na Caixa Atual:       {pecas_na_caixa_atual}/10")
    
    if reprovadas > 0:
        print("\nMotivos de Reprovação:")
        cursor.execute("SELECT id, motivo FROM pecas WHERE status = 'Reprovada'")
        for r in cursor.fetchall():
            print(f"- Peça {r[0]}: {r[1]}")
    print("="*35)
    conn.close()

# --- INTERFACE DE USUÁRIO (MENU) ---

def menu():
    iniciar_db()
    while True:
        print("\n🏭 SISTEMA DE QUALIDADE INDUSTRIAL")
        print("1. Cadastrar nova peça")
        print("2. Listar peças cadastradas")
        print("3. Remover peça (ID)")
        print("4. Relatório final")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            id_rem = input("Digite o ID da peça para remover: ")
            excluir_peca(id_rem)
            print(f"Comando de remoção para ID {id_rem} executado.")
        elif opcao == '4':
            gerar_relatorio()
        elif opcao == '0':
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()