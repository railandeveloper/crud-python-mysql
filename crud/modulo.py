from conexao import conexao  # só pega o objeto de conexão

def menu():
    print("\n===== MENU CRUD =====")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("5 - Sair")
    print("======================")


def Cadastrar_usuario():
    cursor = conexao.cursor()
    nome = str(input(' Nome: ')).strip()
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print(f'Digite apenas numeros inteiros para a Idade')
            continue
        if  idade >= 1:
            break
        else:
            print(f'A idade deve ser um numero positivo')        
    cursor.execute('INSERT INTO pessoas (nome, idade) VALUES (%s, %s)', (nome, idade))
    conexao.commit()
    cursor.close()
    
    
    

def listar_usuarios():
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM pessoas')
    lista_de_pessoas = cursor.fetchall()
    
    if not lista_de_pessoas:
        print('Nenhum usuário cadastrado.')
    else:
        print('\n📋 Usuários cadastrados:')
        for id, nome, idade in lista_de_pessoas:
            print(f'ID: {id} | Nome: {nome.capitalize()} | Idade: {idade}')
    cursor.close()
    
    
def Atualizar_dados_do_usuário():
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM pessoas')
    lista_de_pessoas = cursor.fetchall()
    if not lista_de_pessoas:
        print('Nenhum usuário cadastrado.')
    else:
        listar_usuarios()   
        while True:   
            try:
                id_escolhido = int(input('digite o id da pessoa que deseja alterar os dados: '))
            except ValueError:
                print(f'O id deve ser um numero inteiro')
                continue 
            id_encontrado = False
            for id, nome, idade in lista_de_pessoas:
                if id == id_escolhido:
                    id_encontrado = True
            if id_encontrado:
                break    
            else:
                print(f"id invalido, verifique os id's disponiveis")
                continue
                         
        escolha = str(input(f'Voce deseja alterar o nome ou a idade responda com [nome/idade]?: ')).strip().lower()
        if escolha == 'nome':
            novo_nome = str(input('Digite o nome com os novos dados: '))
            cursor.execute('UPDATE pessoas SET nome = %s WHERE id = %s', (novo_nome, id_escolhido))
            conexao.commit()
            print('nome alterado com sucesso!')
            cursor.close()

        elif escolha == 'idade':
            while True:
                try:
                    nova_idade = int(input('Digite a idade: '))
                except ValueError:
                    print(f'a idade deve ser um numero inteiro')
                    continue
                if nova_idade > 0:        
                    cursor.execute('UPDATE pessoas SET idade = %s WHERE id = %s', (nova_idade, id_escolhido))
                    conexao.commit()
                    print('idade alterada com sucesso!')
                    cursor.close()
                    break
                else:
                    print(f'A idade deve ser um numero valido')
        
        else:
            print(f'escolha invalida responda com [nome/idade]')
            
                
        
def deletar_dados():
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM pessoas')
    lista_de_pessoas = cursor.fetchall()
    if not lista_de_pessoas:
        print('Nenhum usuário cadastrado.')
    else:
        listar_usuarios()
        while  True:
            try:
               id_escolhido = int(input('digite o id da pessoa que deseja deletar os dados: '))
            except ValueError:
                print('Digite um numero inteiro para o id')
                continue    
            
            id_encontrado = False
            for id, nome, idade in lista_de_pessoas:
                if id == id_escolhido:
                    id_encontrado = True
            
            if not id_encontrado:
                print("Id não encontrado")
                continue        
            
            if id_encontrado:        
                cursor.execute('SELECT * FROM pessoas Where id = %s', (id_escolhido,))
                pessoa_escolhida = cursor.fetchone()
                print(f'Dados a serem deletados: ID: {pessoa_escolhida[0]} | Nome: {pessoa_escolhida[1].capitalize()} | Idade: {pessoa_escolhida[2]}')
                confirmacao = str(input(F'Tem certeza que deseja deletar os dados [S/N]: ')).strip().upper()
                
                if confirmacao == 'S':
                    cursor.execute('DELETE FROM pessoas WHERE id = %s', (id_escolhido,))
                    print(f'Dados apagados com sucesso')
                    conexao.commit()
                    cursor.close()
                    break
                    
                elif confirmacao == 'N':
                    print('Deletar dados cancelado.')
                    break      
                else:
                    print(f'opcao invalida')      
            
           
         
               
            
                   
        
                