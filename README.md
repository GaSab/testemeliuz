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
Dentro da pasta notebooks dentro do projeto existe um pequeno notebook contendo a exploração de dados feita para testar e descobrir quais eram os produtos desejados a serem retornados.


# Implementação
Implementei a solução utilizando Django.
É uma implementação bem simples apenas com uma view chamada new_user_sugestion e apenas a request do tipo post nfoi implementada, apesar de existire mocks dos outros tipos.
A request uma vez chamada faz a query queries/retrieve_most_sold.py e retorna seu conteudo que seria a resposta explicada na sessão da heuristica utilizada.
Foram usados serializers para parsear o conteudo das respostas.

# Testes
Eu construi basicamente 3 testes de funcionalidade:
- O primeiro é simples apenas testando que dado que o banco está alimentado, quando a api é chamada ela responde e o resultado bate com o resultado esperado (resultado esperado está em salesdata/data_demos/demo_json).
- O segundo é, dado que o banco esteja alimentado, ao inserir um novo produto com mais vendas que os outros anteriores, se ele seria retornado e o resultado seria o esperado.
- O terceiro é o oposto do segundo, utilizando um podutos com menos vendas que os padrões ele nao deve entrar no resultado.
