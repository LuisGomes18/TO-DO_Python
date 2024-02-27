# TODO List em Python

Este é um simples aplicativo de lista de tarefas (TODO) desenvolvido em Python. Ele permite que os usuários criem, visualizem, marquem como concluídas e excluam tarefas da lista.

## Funcionalidades

- Adicionar uma nova tarefa à lista.
- Visualizar todas as tarefas na lista.
- Marcar uma tarefa como concluída.
- Excluir uma tarefa da lista.

## Pré-requisitos

- Python 3 instalado.
- Bibliotecas `mysql-connector-python`.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LuisGomes18/TO-DO_Python.git
```
<br>

2. Navegue até o diretório do projeto:

```bash
cd TO-DO_Python
```
<br>

3. Crie um ambiente virtual em python
```bash
python3 -m venv .venv
```

3.1. Ative o ambiente virtual em Windwos
````bash
.venv\Scripts\activate
````

3.2. Ative o ambiente virtual no Linux ou MacOS
````bash
source .venv/bin/activate
````
<br>

4. Instale as dependencias necessarias
````bash
pip freeze > requirements.txt
````
<br>

4. Execute o script sem gui:

```bash
python3 main_sem_gui.py
```

4.1. Execute o script com gui:
```bash
python3 main_sem_gui.py
```
<br>

## Uso

- Ao executar o aplicativo, você será apresentado com um menu de opções.
- Escolha a opção desejada digitando o número correspondente.
- Siga as instruções na tela para adicionar, visualizar, marcar como concluída ou excluir tarefas.
<br>

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs ou novas funcionalidades.
<br>

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
