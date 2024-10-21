# Ouvidoria Web

![Logo da Ouvidoria](https://img.icons8.com/?size=100&id=37212&format=png&color=000000)  <!-- Substitua pelo caminho da sua logo -->

## Descrição
A Ouvidoria Web é uma aplicação desenvolvida em Django, que permite a gestão de denúncias, reclamações, elogios e sugestões. Esta aplicação fornece um CRUD completo para gerenciar as interações dos cidadãos de forma eficiente e transparente.

## Funcionalidades
- **Cadastro de Denúncias**: Permite que os usuários cadastrem denúncias com informações detalhadas e acompanhar o status.
- **Cadastro de Reclamações**: Usuários podem registrar reclamações e acompanhar o status.
- **Cadastro de Elogios**: Possibilidade de registrar elogios para serviços ou atendimentos e acompanhar o status.
- **Cadastro de Sugestões**: Usuários podem enviar sugestões para melhorias e acompanhar o status.
- **Listagem de Registros**: Visualização de todas as denúncias, reclamações, elogios e sugestões cadastradas.
- **Feedback e Status**: O sistema permite que os usuários recebam feedback sobre suas interações.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.12.7
- **Framework**: Django 5.1.2
- **Gerenciador de Dependências**: Pip
- **Banco de Dados**: SQLite
- **Estilização**: Tailwind CSS


## Como Executar o Projeto

### Pré-requisitos:
- Python 3.12.7
- Django 5.1.2


### Clone o Repositório:

```bash
git clone https://github.com/CaioEmannuelDiniz/projeto_ouvidoria_web.git
```

### Altere o Arquivo .env.examples:
- Altere o nome do arquivo `.env.example` para apenas `.env`
- Defina os valores correspondente para cada variável

### Instale as Dependências:
```
pip install -r requirements.txt
```

### Execute as Migrações:
```
python manage.py migrate
```

### Inicie o Servidor:
``` 
python manage.py runserver
```

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Faça commit das suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT.

## Contato

Se você tiver dúvidas ou sugestões, entre em contato:

- **LinkedIn**: [Caio Emannuel](https://www.linkedin.com/in/caio-emannuel-diniz/)

## Agradecimento
Agradeço por conferir o `Ouvidoria Web!` Espero que este projeto seja valioso e inspire novas ideias. Boa leitura! 📚
