Os 3 pilares da observabilidade:
    -> Metrics
    -> Traces
    -> Logs

    Metrics:
        - Quando falamos em analisar metricas, estamos basicamente falando em analisar o estado de uma determinada medida em um dado momento. Normalmente elas são apresentadas usando gráficos/diagramas de tempo, onde é possível visualizar todo o comportamento daquela medida em um certo intervalo de tempo. Exemplos mais comuns são: gráficos de utilização de CPU, temperatura de CPU e entre outros. Existem duas métricas que são mais populares, utilization e saturation, sendo a utilização literalmente o nível de utilização de certo recurso, como uma CPU por exemplo. Já a saturação é mais sobre a sobrecarga do recurso, sobre o quanto a demanda excede a capacidade de trabalho do recurso. Para deixar mais claro, um recurso com 100% de utilização não é necessariamente um problema, mas, a partir do momento em que a saturação começa a subir, quer dizer que uma fila está se formando, ou seja, existem processos esperando para serem processados. Isso geralmente vem acompanhado de um aumento de latência, o que impacta diretamente o usuário final, que vai ter que esperar um tempo maior para obter o resultado da sua requisição. Existem 3 tipos chaves de métricas:

            - Counters: Medidas acumulativas que só podem crescer. Ex: número total de requisições;
            - Gauges: Medidas que podem crescer ou decrescer. Ex: número de agentes ativos;
            - Histograms: Distribuição de valores ao longo do tempo. Ex: tempo para o primeiro token;

    Traces:
        - Os traces são extremamente importantes em um processo de observabilidade, pois elas permitem visualizar todo o caminha que a requisição fez, por quais serviços passou, quanto tempo levou em cada, quais chamadas foram feitas e entre outras métricas. Antes de continuar, é importante explicar o conceito de "Spans", um span é um ponto específico nesse caminho, como uma chamada de função ou uma consulta em um banco de dados, por exemplo. Entrando no contexto de sistemas multiagenticos, que são sistemas não determinísticos e assíncronos, traces vão ajudar a saber em qual etapa do fluxo de pensamento do agente que ocorreu o erro, ou então ver como que está o desempenho de uma etapa específica desse fluxo. Com exemplo, casos onde o sistema está em loop infinito, você veria que a trace iria mostrar uma sequencia infinita de spans idênticos, ou para ver gargalos nos agentes, como se um agente está demroando muito para passar a requisição para frente. Um fato interessante, é que as traces possuem IDs únicos e, para no final, haver uma trace completa e correta é necessário que ocorre uma propagação de contexto correta. Em um sistema multiagentes, cada agente precisa injetar o trace id na janela de contexto do próximo agente, para que assim esse próximo agente consiga trabalhar em cima da mesma trace e naquele mesmo contexto e, caso isso não ocorra de forma correta, ocorre a quebra da trace, ou seja, os agentes perdem a conexão uns com os outros.

    Logs:
        - Os logs são basicamentes relatórios de estado da execução de um sistema. Normalmente possuem mensagens de erros, stack traces, mudanças de estado da aplicação, ações do usuário, eventos do sistema e informações detalhadas de transações. Por mais que os logs sejam muito úteis, eles também geram alguns desafios e possuem algumas limitações, como: 
            - Alto volume: Um sistema pode gerar uma quantidade enorme de logs, o que dificulta a análise e o armazenamento. Isso também pode afetar no desempenho da aplicação.
            - Dados não estruturados: Por mais que existem ferramentas para auxiliar nessa parte, os logs podem vir sem uma estrutura definida, dificultando a análise.
            - Consistência: Em aplicações mais complexas, como sistemas distribuídos por exemplo, é complicado conseguir manter práticas de logs semelhantes, o que também pode dificultar a análise.

        Sabendo disso, os logs também são essenciais na observabilidade, pois enquanto as métricas te alertam, as traces te mostram onde ocorreu o erro, os logs te mostram o que é o erro e por que esse erro ocorreu. Por exemplo, no seu sistema ocorreu um erro e você viu na trace que foi em um span específico, com isso você filtra os logs para os que possuem aquele trace id e verifica o que ocorreu e por que ocorreu, por exemplo "Erro ao conectar na API".

Fonte: https://signoz.io/blog/three-pillars-of-observability/


