
from create_b_d import Usuario, session
from datetime import datetime


nome_busca = input("Digite seu nome para acessar: ")

usuario_existente = session.query(Usuario).filter_by(nome=nome_busca).first()

if usuario_existente:
    print(f"\nBem-vindo de volta, {usuario_existente.nome}!")
    print(f"Seu e-mail cadastrado é: {usuario_existente.email}")
else:
  
    print("\nUsuário não encontrado! Por favor, realize o cadastro.")
    
    email_novo = input("Digite o e-mail para cadastro: ")
    id_arquivo_novo = input("Digite o ID do arquivo (ou pressione Enter): ")

    novo_usuario = Usuario(
        nome=nome_busca, 
        email=email_novo,
        arquivo_id=id_arquivo_novo
    )

    try:
        session.add(novo_usuario)
        session.commit()
        print(f"Cadastro realizado com sucesso para {nome_busca}!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao cadastrar: {e}")


print("\n Lista Atual de Usuários")
todos = session.query(Usuario).all()
for user in todos:
    print(f"Nome: {user.nome} | Email: {user.email}")
