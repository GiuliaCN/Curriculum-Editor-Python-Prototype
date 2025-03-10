# Edição de Currículos - Python

Este projeto tem como objetivo criar uma ferramenta simples para editar, formatar e gerar currículos no formato PDF. A ferramenta permite carregar um arquivo de texto com as seções do currículo, selecionar seções e subseções, gerar um PDF formatado com base no texto carregado, e salvar configurações para reutilização futura.

## Funcionalidades

- **Carregar arquivo de currículo**: Importa um arquivo de texto com as seções do currículo.
- **Reconhecimento de seções**: Identifica e permite a seleção de seções e subseções do currículo.
- **Geração de PDF**: Formata e gera um currículo no formato PDF.
- **Salvar configurações**: Permite salvar preferências de formatação e configurações para uso futuro.

## Tecnologias

- **Python 3.x**: A linguagem de programação principal do projeto.
- **Tkinter**: Usado para criar a interface gráfica (GUI).
- **ReportLab**: Biblioteca para gerar PDFs a partir do conteúdo editado.
- **Regular Expressions (Regex)**: Utilizado para identificar e organizar as seções do currículo no texto.

## Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, é necessário ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

### Instalação

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/GiuliaCN/Curriculum-Editor-Python-Prototype.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd edicao-curriculo-python
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o projeto:

    ```bash
    python main.py
    ```

### Estrutura de Arquivos

- `main.py`: Arquivo principal que inicializa a aplicação.
- `curriculo.txt`: Exemplo de arquivo de currículo em formato texto.
- `requirements.txt`: Lista de dependências do projeto.
- `utils.py`: Funções auxiliares para manipulação de textos e PDFs.

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias para melhorar a ferramenta ou encontrar algum bug, fique à vontade para abrir um *issue* ou um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
