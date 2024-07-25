# Testemeliuz
Essa é minha implementação da solução para o desafio tecnico da meliuz.

# Heuristica
Escolhi utilizar uma euristica que retorna 5 registros da lista enviada baseado nas 3 seguintes metricas, em ordem:

1) Os 5 produtos com mais vendas totais.
    Aqui decidi não filtrar por periodo (5 mais vendidos no ultimo mes), pois me pareceu menos relevante no contexto, mas poderia ser adicionado facilmente essa caracteristica.
    Escolhi essa como principal ponto pois acredito que sem dados do cliente em si apostar nos maiores sucessos de vendas é uma boa aposta para direcionar.
2) As lojas que mais vendem cada produto.
    Conhecidos os produtos a serem enviados os registros as serem enviados são os das lojas que mais venderam cada um deles.
    Acredito que lojas que vendem mais um produto seriam ideais pois provavelmente guardam mais estoque, tem prazos menores de entrega e outros tipos de facilidades que facilitam e tornam a venda mais interessante e provável.
3) Caso uma loja tivesse mais de um registro decidi por utilizar o registro com o maior id
    Essa foi só um detalhe, mas também notei que caso fosse um banco real e por exemplo também contesse um link do anuncio, um id maior em geral significa um registro mais novo, que pode nos indicar anuncios mais ativos e/ou com vendas mais recentes (ou seja, que funcionam) assim aumentando a probabilidade que aquilo seja um anuncio valido, bom e saudavel, assim aumentando a chance de finalizar a venda.

Para a implementação construi um pequeno banco sqlite e tranferi os dados da tabela fornecida utilizando o script filltable.
O modelo da tabela está em salesdata/models/salesdata
Para recuperar os dados dos 5 registros escolhidos existe uma query sql no script queries/retrieve_most_sold.py que contem a pesquisa que é chamada.

# Exploração dos dados
- Dentro da pasta notebooks dentro do projeto existe um pequeno notebook contendo a exploração de dados feita para testar e descobrir quais eram os produtos desejados a serem retornados.


# Implementação
- Implementei a solução utilizando Django.
- É uma implementação bem simples apenas com uma view chamada new_user_sugestion e apenas a request do tipo post nfoi implementada, apesar de existire mocks dos outros tipos.
- A request uma vez chamada faz a query queries/retrieve_most_sold.py e retorna seu conteudo que seria a resposta explicada na sessão da heuristica utilizada.
Foram usados serializers para parsear o conteudo das respostas.

# Testes
Eu construi basicamente 3 testes de funcionalidade:
- O primeiro é simples apenas testando que dado que o banco está alimentado, quando a api é chamada ela responde e o resultado bate com o resultado esperado (resultado esperado está em salesdata/data_demos/demo_json).
- O segundo é, dado que o banco esteja alimentado, ao inserir um novo produto com mais vendas que os outros anteriores, se ele seria retornado e o resultado seria o esperado.
- O terceiro é o oposto do segundo, utilizando um podutos com menos vendas que os padrões ele nao deve entrar no resultado.

# Execução
>>>>DOCKER

- O projeto contem um arquivo dockerfile  que pode ser transformado em uma imagem utilizando 
docker build -t testmeliuz .
e executado utilizando
sudo docker run -p 8000:8080 testmeliuz
esse ultimo acontece pois pedi para dentro do docker a aplicação executar na porta 8080 e os parametros -p 8000:8080 ligam a porta 8000 local a porta 8080 da maquina docker.

- Para testar a aplicação pode ser realizada uma chamada no endereço 127.0.0.1:8000/nus e ele retornará os 5 produtos mais vendidos seguindo a heurística.
como o banco já está fixo la não são possiveis ainda mudanças.
Infelizmente não implementei opções de adicionar mais registros no endpoint de modo a permitir a alteração desses dados.

>>>>LOCAL

É possivel também utilizar a aplicação de modo local.
- Para isso é sugerida a versão 3.10.12 do python.
- Caso queira utilizar o metodo, após iniciar um novo venv rode o comando pip install -r requirements.txt para instalar as dependencias necessarias para rodar o projeto.
- Depois disso pode navegar ao diretorio principal da aplicação em apimeliuz.
- No caso de execução local é possivel adicionar novos dados substituindo a tabela xpto_sales_products_mar_may_2024.csv - Página4 por uma de mesmo nome e executando o comando python manage.py shell < filltable.py que executa o script que apaga os dados antigos e alimenta eles com o do arquivo fornecido.
- Para executar os testes unitarios pode se usar coverage run --source='.' manage.py test
- Para visualizar o report dos testes utilizasee coverage report 
- É importante lembrar que esses testes foram concebidos com esses dados fornecidos para conferir o funcionamento.
- Para rodar a aplicação pode-se usar python manage.py runserver
- Daqui o funcionamento seria o mesmo do docker acessando o endereço 127.0.0.1:8000/nus a api retornará os 5 itens como projetado

# Limitações e Possíveis Melhorias
Como apontado anteriormente essa aplicação só tem a função de retornar os 5 produtos algumas melhorias seriam:
- Criar capacidade de adicionar novos dados através de API.
- Capacidade também de resetar o banco em novas builds atraves de outros documentos rodando o filltable.
- Talvez separar essa sugestão de uma busca direta nos dados transformar ela em algum tipo de visão assim o get só retornaria o que estaria nessa visao já que também é um conjunto padrão para qualquer novo usuario eai caso, como apontado no proprio enunciado do teste, houvesse o chaveamento entre usuario novo e usuario já com dados seria entre chamar essa ou outra visao. Isso provavelmente ajudaria na velocidade da consulta, ainda mais quando o conjunto de dados for bem maior que esse os agrupamentos e filtros poderiam adicionar mais tempo na busca da query. A ideia aqui seria transformar a busca que tem aqui na verdade em uma busca que estaria no PUT ou POST que ativaria na faria essa busca e consolidaria o resultado na viwew, nao ficando por exemplo em tempo de carregamento da pagina, e sim sendo executadas por processos de atualizaçãom em segundo plano. Enquanto o get seria apenas um SELECT * FROM view_new_user, por exemplo. 
- Nessa implementação eu simplifiquei varias questões para evitar trabalho a mais na implementação que nunca seriam feitas de fato numa aplicação real como ignorar csrf (conferencia de origem da chamada).
