'''📝 Enunciado – CRUD de Usuários com MySQL e Python
Você foi contratado para criar um sistema simples de gerenciamento de usuários, utilizando Python para interagir com um banco de dados MySQL.

Sua missão é criar um programa que:

Conecte-se ao banco de dados crud_python

Apresente um menu interativo com as seguintes opções:

1️⃣ Cadastrar novo usuário

2️⃣ Listar todos os usuários

3️⃣ Atualizar um usuário (por ID)

4️⃣ Deletar um usuário (por ID)

5️⃣ Sair do programa

O programa deve aceitar entradas do usuário no terminal (via input).

Cada operação deve realizar a ação no banco de dados e informar se foi concluída com sucesso.

👤 Tabela: usuarios
id (INT, auto_increment, chave primária)

nome (VARCHAR)

idade (INT)

🧠 Requisitos:
Use mysql.connector para a conexão com o banco

Use cursor.execute() para os comandos SQL

Use commit() quando for inserir, atualizar ou deletar

Trate erros simples como ID inexistente ao atualizar ou deletar

🎯 Objetivo final: Quando rodar o script, ele deve funcionar como um mini sistema de terminal que o usuário pode usar para gerenciar a tabela usuarios.

Quando terminar ou quiser ajuda com um trecho específico, me chama.
Bora fazer esse sistema do zero e depois subir pro seu GitHub com orgulho! 🚀'''