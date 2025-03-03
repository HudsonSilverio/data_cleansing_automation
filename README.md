# Data Cleansing Automation

## About the project

This application is intended to load CSV files with a very large size, perform form cleaning according to your business rules to be defined. 

### Main Ojectives:

 * **Upload an excel file up to a million rows**.
 * **Perform cleanup on loaded data.**
 * **Project to be used by the entire team independently.**

* **Entender a estrutura padrão de projetos**: Isso inclui a organização de diretórios, como o código-fonte, testes, documentação, entre outros.

## Começando

### Pré-requisitos

* **VSCode**: É o editor de código que vamos utilizar no workshop. [Instruções de instalação do VSCode aqui](https://code.visualstudio.com/download).

* **Git e GitHub**:

1. Você deve ter o Git instalado em sua máquina. [Instruções de instalação do Git aqui](https://git-scm.com/book/pt-br/v2).
2. Você também deve ter uma conta no GitHub. [Instruções de criação de conta no GitHub aqui] (https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account).
3. Se você for usuário Windows, recomendo esse vídeo: [Youtube](https://www.youtube.com/watch?v=_hZf1teRFNg).
4. Tutorial de Git e Github básico [Ebook](https://www.linkedin.com/feed/update/urn:li:activity:7093915148351864832/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7093915148351864832%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=4GUdvXH4TK%2BtZtlNHmiqJA%3D%3D).
5. Se você já é usuário Git, recomendo o vídeo do Akita: [Youtube](https://www.youtube.com/watch?v=6Czd1Yetaac).

* **Pyenv**: É usado para gerenciar versões do Python. [Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation). Vamos usar nesse projeto o Python 3.11.3. Para usuários Windows, é recomendado assistirem esse tutorial [Youtube](https://www.youtube.com/watch?v=TkcqjLu1dgA).

* **Poetry**: Este projeto utiliza Poetry para gerenciamento de dependências. [Instruções de instalação do Poetry aqui](https://python-poetry.org/docs/#installation).Se você é usuário Windows, recomendo assistir esse vídeo: [Youtube](https://www.youtube.com/watch?v=BuepZYn1xT8). Que instala o Python, Poetry e VSCode. Mas um simples comando PIP INSTALL POETRY já resolve.

Sugestão de leituras.
[Ebook 1 - Testes](https://www.linkedin.com/feed/update/urn:li:activity:7099722252144848896/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7099722252144848896%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=hg1%2BufBeTLClrS%2BJixGEoA%3D%3D)
[Ebook 2 - Github Actions](https://www.linkedin.com/feed/update/urn:li:activity:7098264928553201665/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7098264928553201665%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=%2BFcdPRcDT62iNieFV3Yc%2Fg%3D%3D)
[Ebook 3 - Na minha máquina funciona](https://www.linkedin.com/feed/update/urn:li:activity:7095419109449814017/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7095419109449814017%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=7ShpQeNCQuCDErI%2BAzEBXw%3D%3D)

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/HudsonSilverio/data_cleansing_automation.git
cd data_cleansing_automation
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Configurar poetry para Python version 3.12.1 e ative o ambiente virtual:

```bash
poetry env use 3.12.1
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Construir a imagem Docker

```bash
docker build -t meu-app .
```

6. Rodar o container.

```bash
docker run -p 8501:8501 meu-app
```

8. Verifique se irá aparecer para voce esse link no terminal para acessar ou irá abrir de forma automatica.

```bash
 http://localhost:8501
```

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Hudson Silvério** - [hudsonpksj@gmail.com](mailto:hudsonpksj@gmail.com)