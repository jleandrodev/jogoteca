# Listando Jogos com Flask

Este é um pequeno aplicativo Flask que cria uma lista de jogos e permite que o usuário adicione novos jogos à lista. Ele também inclui um sistema de login básico para proteger a rota de adicionar jogos.

  

## Como funciona

Ao executar o código, o Flask cria um servidor local em que o usuário pode interagir com o aplicativo. Existem quatro rotas:

  

- A rota raiz exibe a lista atual de jogos.

- A rota **'/novo-jogo exibe'** um formulário para que o usuário adicione um novo jogo à lista. Essa rota só é acessível para usuários logados.

- A rota **'/criar'** é acionada quando o usuário envia o formulário. Ela cria um novo objeto Jogo com base nas informações fornecidas no formulário e adiciona o objeto à lista de jogos.

- A rota **'/login'** exibe um formulário de login.

- A rota **/autenticar **é acionada quando o usuário envia o formulário de login. Se a senha fornecida for correta, a rota salva o nome do usuário na sessão e redireciona para a rota raiz. Caso contrário, a rota exibe uma mensagem de erro e redireciona para a rota de login.

- A rota **'/logout'** limpa a sessão do usuário e redireciona para a rota raiz.

  

## Como usar

Clone o repositório em sua máquina local.

Certifique-se de ter o Flask instalado em sua máquina **(pip install Flask)**.

Execute o arquivo **'jogoteca.py'** em seu terminal **(python jogoteca.py)**.

Abra um navegador e vá para **http://localhost:5000/** para ver a lista de jogos.

Para adicionar um novo jogo à lista, faça login clicando em Login na barra de navegação e preenchendo o formulário. Depois, vá para **http://localhost:5000/novo-jogo** e preencha o formulário.

Para fazer **'logout'**, clique em Logout na barra de navegação.