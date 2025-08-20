import sqlite3

# Conectar ao banco (vai criar banco.db no ambiente do Colab)
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

def inserir_usuario(nome, email):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

def atualizar_usuario(id, novo_nome, novo_email):
    cursor.execute("UPDATE usuarios SET nome=?, email=? WHERE id=?", (novo_nome, novo_email, id))
    conexao.commit()

def deletar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conexao.commit()
# Inserir usuários
inserir_usuario("João", "joao@email.com")
inserir_usuario("unicid", "iunicida@email.com")

# Listar
print(listar_usuarios())