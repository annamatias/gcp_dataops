![Apache Spark](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)![GitHub Actions](https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe)![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=Databricks&logoColor=white)![Delta Table](https://camo.githubusercontent.com/8dc907a1f537c017900e758ac8eb0b595090567c431a5e9fc993ae1cbf8379e4/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d44656c746126636f6c6f723d303033333636266c6f676f3d44656c7461266c6f676f436f6c6f723d464646464646266c6162656c3d)
<h1 align="center">GCP DataOps</h1>

<p align="center">Projeto com todos os processos de DataOps</p>

[![Pylint](https://github.com/annamatias/gcp_dataops/actions/workflows/pylint.yml/badge.svg)](https://github.com/annamatias/gcp_dataops/actions/workflows/pylint.yml)

# Sobre

<p>O projeto representa todos os processos de DataOps, ele contém CI/CD, criado com o Actions Workflows do GitHub para podermos testar o código após o push. Trazendo mais segurando e uniformidade ao código, evitando futuros erros na execução, e integridade ao dividir o código entre a equipe. Estamos utilizando do Google Cloud Platform, para utilização IaaS (Infraestrutura como Serviço), usufruindo da Compute Engine, Databricks e Storage Cloud.</p>
<p>O desenvolvimento da ingestão de dados, estaremos utilizando das tecnologias: Python, Pyspark e Delta Lake. Esquematizando a visualização de dados, utilizaremos do próprio Databricks, e finalizando o fluxo de DataOps, ele deve conter Data Observability e Data Monitoring, nossa infraestrutura ela já consta com otimas ferramentas de monitoração da nossa aplicação, e para fecharmos com chave de ouro iremos utilizar dos loggers, para garantir rastreabilidade de erros no nosso código.</p>
<p>Sem contar que para entregarmos dados com a qualidade, esse projeto conta com boas práticas de Data Quality e testes unitários feito em pyspark, para além de testarmos o resultado esperado e nossas funções, atendermos os pilares de qualidade dos dados, entre eles: precisão, completude, consistência, validade, exclusividade e pontualidade.</p>

> *Até então, não é ideal utilizar spark para a pequena quantidade de dados, o ideal é acima de GB (Giga Bytes), mas é um projeto, visa trazer aprendizados da vida real, com conteúdo técnico.*


---

# Executar Projeto

Você pode realizar o clone, e executar o jupyter notebook, mas não vai funcionar como é o verdadeiro objetivo (Utilizar o GCP para execução juntamente com o Databricks).

Para executar o meu projeto, recomendo criar uma conta no google cloud platform, caso não tenha e realizar os passos abaixo de configuração e execução. Nessa doc do projeto tem todos os passos para reproduzir um equivalente ao meu, mas é necessário apenas configurar a conta e importar o arquivo e executar no ambiente configurado.

## Clonagem

`> git clone https://github.com/annamatias/gcp_dataops.git`

---

# Configurando GCP (Google Cloud Platform)

Depois que criamos nossa conta, ele já cria um projeto automaticamente, para termos controle de qual projeto estamos mexendo, vamos renomear.

No canto superior direito, ao lado esquerdo da sua foto de perfil da conta do google, temos um menu, iremos clicar nele e ir até **Configuração do projeto**, conforme imagem abaixo. Eu coloquei o nome de **Databricks with GCP**, fique a vontade para escolher o seu.

<p align="center"><img width="489" alt="image" src="https://github.com/annamatias/dataengineer-google-cloud/assets/53863170/890fba52-e43d-4fcb-9ded-6eb3fcdb5aee"></p>
<p align="center">imagem 1 - Acessando configurações</p>

<p align="center"><img width="542" alt="image" src="https://github.com/annamatias/dataengineer-google-cloud/assets/53863170/196173f6-9ca3-421d-bc03-4eec19d29aa0"></p>
<p align="center">imagem 2 - Alterando nome do projeto e salvando</p>

# Ativando Databricks

No canto superior esquerdo, temos um menu bar, acessando ele, vamos atrás do **Databricks**, o GCP te trás opção de fixar para aparecer logo em cima. Eu fixei para encontra-lo com maior facilidade.

<p align="center"><img width="410" alt="image" src="https://github.com/annamatias/dataengineer-google-cloud/assets/53863170/fc938654-795f-4a00-b081-d8ef7fa1e317"></p>
<p align="center">imagem 4 - Databricks fixado</p>

Depois que acessar o databricks, clique em Assinar e concorde com os termos e condições.
Antes do botão acessar, irá mostrar o resumo do pedido e quantidade de dias que estará gratuito.

> Outro ponto importante você tem que ter um cartão para faturamento, mas fica calmo que a Google não vai sair cobrando nada de você. Muito pelo contrario e é uma experiencia muito boa que eu obtive, quando passa o prazo de gratuidade e você não assina o pacote completo, ele automaticamente apaga e corta os recursos utilizados para não gerar nada, e você não será cobrado.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/e804f57d-604e-4985-8382-9695a637828d"></p>
<p align="center">imagem 3 - Resumo do pedido, ao assinar o Databricks</p>

Faça login sempre com a conta que utiliza o GCP, depois que selecionar o plano que eles indicam para você criar a conta no Databricks, e vai aparecer uma tela conferme a próxima imagem. Observe que eles pedem o nome de uma organização, você escreve o nome que achar melhor.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/f4bcde57-7ae7-45eb-a977-5bf0fe14b31a"></p>
<p align="center">imagem 5 - Criando conta</p>

Feito o processo acima, importante citar que vai ser enviado um e-mail com a confirmação da criação da conta, parecido com o e-mail abaixo.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/a92090c3-25d2-4706-b476-61f362ef03c5"></p>
<p align="center">imagem 6 - Exemplo e-mail</p>

Depois que chegar o e-mail, volte novamente na console do GCP na aba do Databricks. Iremos clicar em "Gerenciar no fornecedor" nele, ele vai te redirecionar para um link para você fazer login e criar o seu **workspace**. Antes disso, iremos realizar login novamente e selecionar o plano de assinatura, é só confirmar.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/ae8a9d96-27ef-4255-be81-17112db2fe7d"></p>
<p align="center">imagem 7 - Gerenciar no fornecedor</p>

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/33690575-f774-472e-a6a6-81b10f94c836"></p>
<p align="center">imagem 8 - Plano de assinatura</p>

Feito os passos acima, ele vai abrir o workspace, conforme dissemos anteriormente, iremos criar o nosso "Criar Workspace".

Aqui nesse passo é bem simples. Basta colocar o nome do workspace que deseja, você vai copiar do GCP o ID do projeto e colar lá, e na região SEMPRE busque utilizar `us-central1` porque esse é uma das regiões gratuitas.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/41cb92e9-ce89-4dcb-9d5f-ee9787e68cc4"></p>
<p align="center">imagem 9 - Configuração workspace</p>

Feito isso, você vai finalizar e vai receber um **email**, lá vai ter o link que está apto a mexer no databricks, ou então você pode clicar logo em seguida no workspace que criou e aguardar o link ser disponibilizado, conforme exemplo abaixo.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/d88715ec-1bfd-4d64-8013-0a8e9bb34155"></p>
<p align="center">imagem 10 - Workspace preparando o link</p>

Acessando o link, vamos criar um cluster, ele já aparece logo no inicio bem grande, ele já vai criar com as configurações necessárias para você mas você pode alterar de acordo com a necessidade. Como é um projeto simples vou deixar do jeito que está.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/f1701071-639f-40ea-9227-ad907b9531c4"></p>
<p align="center">imagem 11 - Criando cluster</p>

## Gratuidade

> Reforçando recado IMPORTANTE!

O GCP é gratuito por 90 dias para novos usuários e o Databricks por 14 dias (Lembrando que os prazos sempre estão sujeito a alterações).
Fique sempre atento a esse prazo, para que não tenha eventuais cobranças futuramente.

O próprio google alega que depois de 90 dias caso não tenha o upgrade, ele exclui todos os seus projetos, mas faça isso antes..."O seguro morreu de velho" - Como diz meus pais.

# CI/CD GitHub e Databricks

Neste projeto iremos realizar a conexão entre Github e Databricks, para CI/CD. Primeiro vamos conectar o nosso repositório.
> Se você estive utilizando a versão gratuita talvez tenha limitações para conseguir realizar a integração, caso já tenha muitas coisas dentro do repositório.

Para adicionar, devemos ir na sessão de **repositórios**, como a imagem abaixo, adicionar as informações que solicitam, basicamente o link do clone do repo. Feito isso é só criar um repositório.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/df46d52f-1248-40af-ac2c-deed8ae077b8"></p>
<p align="center">imagem 12 - Criando repositório</p>

Concluindo o passo acima, já é possível visualizar o nosso repositório e as pastas.
> O Databricks ele é bem completo, principalmente a sua documentação, onde pela própria interface conseguimos criar uma nova branch, realizar commits, push, pull, merge pela mesma interface.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/f03b0445-98b0-4be1-9c97-a309fcb2c593"></p>


## Github Actions

Para termos nossa esteira de integração e entrega continua, vamos utilizar os workflows do github. Ele vai servir para manter a acuracia do código, para não haver futuros erros e depuração de código demorada para cada usuário que esteja utilizando do repositório.

Estou seguindo essa [documentação do github](https://docs.github.com/pt/actions/automating-builds-and-tests/building-and-testing-python) para implementarmos workflows no python.

### PyLint

Primeiro de todos os workflows, baseado em DataOps, iremos implementar o Lint, ele serve para verificar se a escrita do nosso código está correta, evitando erros futuros, antes mesmo de o código estar em vigor executando.

- [Documentação Lint](https://docs.github.com/pt/actions/automating-builds-and-tests/building-and-testing-python#using-ruff-to-lint-code)

O exemplo a seguir instala ou atualiza o ruff e o usa para fazer lint de todos os arquivos. Para obter mais informações, confira [Ruff](https://beta.ruff.rs/docs/). Dei uma adaptada baseado na doc do github actions, acrescentei o nome, onde ele vai executar e o jobs build.

> Para aplicar, você tem que criar uma nova pasta oculta `.github/workflows` e um arquivo yml, com o conteúdo abaixo.

```yaml
name: Pylint

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with Ruff
      run: |
        pip install ruff
        ruff --format=github --target-version=py37 .
      continue-on-error: true

````

A etapa de lint tem continue-on-error: true definido. Isto impedirá que o fluxo de trabalho falhe se a etapa de limpeza de código não for bem-sucedida. Após corrigir todos os erros de limpeza de código, você poderá remover essa opção para que o fluxo de trabalho capture novos problemas.

### Verificando Build Pylint

O nosso primeiro build, a ideia é que falhe mesmo, porque estamos configurando ele. Como estamos realizando a instalação do requeriments no nosso bash, mas ele não existe ainda. Segue um mini gif, ensinando como verificar o seu build aqui no github.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/e7fb415a-c45c-451c-a67f-89c6bd170d4a"></p>

Mas ele está pronto o nosso build, agora com a implementação do código e executando na máquina local, você consegue realizar testar tudo o que foi instalado no ambiente virtual. Eu comentei esse trecho de dependencias por enquanto para visualizar a funcionalidade e ele funciona lindamente.

<p align="center"><img width="1347" alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/d9d2da6f-8851-48b1-8f85-a403426a6794"></p>
<p align="center">imagem 13 - Execução build pylint</p>

# ETL

## Realizando Pull

Somente seguir o gif abaixo, para realizar o pull após alterações.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/c64bd1f3-80c2-49f2-b03d-12a76bffc054"></p>

## Criando pastas e arquivos dentro do repositório

Exemplo de criação de pastas e notebook dentro de um repositório no Databricks;

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/9154ed17-16a9-4968-bf36-3e1bf5a22041"></p>

## Criando um notebook

Feito tudo acima, agora conseguimos utilizar do nosso cluster.

No canto superior esquerdo vamos em **Data science e engineering**, clique no `+` para criar um notebook.

## Onde está os meus notebooks?

No canto superior esquerdo vamos em **Data science e engineering**, clique em `Workspace` para ver todos os notebooks, pastas criadas dentro do databricks.

## Realizando a importação de um arquivo

Você pode simplesmente baixar e depois arrastas ou procurar via desktop o seu arquivo, e realizar o deploy.

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/f4231d23-8012-4862-aad3-5fd6098f0f2d"></p>

## Realizando upload de arquivo no Storage Cloud

Iremos acessar via console o storage cloud, depois disso é somente adicionar um novo arquivo no caminho desejado. Como vou utilizar o arquivo no databricks, eu adicionei dentro de uma pasta `/tmp`

<p align="center"><img alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/4f23a6df-13eb-401d-874e-43adc44e34ea"></p>


## Como criar um Job com Schedule?

No canto superior esquerdo vamos em **Data science e engineering**, clique em `Workflows` para ver todos os jobs criados, e para criar um novo, você vai no canto superior direito em `Create Job`.

---

# Status do Projeto

Em andamento.

# Arquitetura Base

<p align="center"><img width="1126" alt="image" src="https://github.com/annamatias/gcp_dataops/assets/53863170/4fe5a655-a3f9-484e-ad50-bb1cd30e12ec">
</p>

---

# Referências

- Github
  - <https://docs.github.com/pt/actions/learn-github-actions/understanding-github-actions>
  - <https://docs.github.com/pt/actions/automating-builds-and-tests/about-continuous-integration>
  - <https://docs.github.com/pt/actions/automating-builds-and-tests/building-and-testing-python>
  - <https://docs.github.com/pt/actions/automating-builds-and-tests/building-and-testing-python>
- Data Quality
  - <https://www.heavy.ai/technical-glossary/data-quality>

---

# Autor

**Anna Karoliny** - *Mentora, Professora, Desenvolvedora e Engenheira de Dados*
<div>
<a href="https://www.instagram.com/annaskaroliny/" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
<a href="https://www.linkedin.com/in/anna-karoliny-matias-dos-santos"
target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>
