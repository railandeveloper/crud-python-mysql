import modulo, time 


while True:
    modulo.menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print(f'Digite um numero inteiro')
        continue    

    if opcao == 1:
        print("🔹 Cadastrar usuário")
        modulo.Cadastrar_usuario()
        
    elif opcao == 2:
        print("🔹 Listar usuários")
        modulo.listar_usuarios()
        
    elif opcao == 3:
        modulo.Atualizar_dados_do_usuário()
        print("🔹 Atualizar usuário")
        
    elif opcao == 4:
        modulo.deletar_dados()
        print("🔹 Deletar usuário")
        
    elif opcao == 5:
        print("👋 Saindo...")
        time.sleep(2)
        print(f'programa encerrado')
        break
    else:
        print("⚠️ Opção inválida. Tente novamente.")
