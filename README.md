# Projeto SporteFastAPI

Este projeto utiliza FastAPI para criar uma API que fornece dados de times de futebol do campeonato brasileiro. Além disso, usa Selenium para automação de testes com o navegador Chromium e um script para gerar gráficos com esses dados.

## Introdução

Este projeto demonstra como configurar e usar uma API com FastAPI para fornecer dados de times de futebol do campeonato brasileiro e como gerar gráficos a partir desses dados.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados no seu sistema:

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) (para usuários Windows)
- [FastAPI](https://fastapi.tiangolo.com/) e [uvicorn](https://www.uvicorn.org/)
- [Chromium](https://www.chromium.org/) e [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Instalação

1. Clone este repositório:

    ```sh
    git clone https://github.com/dayvd100/apiAndScrapingSerieA.git
    cd sportefastapi
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

## Configuração

### Baixar e Configurar Chromium e ChromeDriver

1. **Baixe o Chromium**:

    Baixe e instale o Chromium a partir do site oficial: [Chromium](https://www.chromium.org/)

2. **Baixe o ChromeDriver**:

    Baixe o ChromeDriver correspondente à versão do Chromium que você instalou a partir do site oficial: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

    Certifique-se de que o ChromeDriver esteja no seu PATH ou atualize o caminho no script conforme necessário.

## Execução

### Rodando a API
apiAndScrapingSerieA > cd sportGeApi > 
rodar o seguinte script:
```
fastpi dev api_script.py 
```

## Gerando o grafico 
apiAndScrapingSerieA > cd generatingGraphic > 
rodar o seguinte script:
```
python3|python graphic.py
```
