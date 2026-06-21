📊 Análise de Filtro RC no Domínio da Frequência
📌 Sobre o Projeto

Este repositório apresenta um experimento prático da disciplina Sinais e Sistemas, realizado na UFERSA – Campus Pau dos Ferros, com o objetivo de analisar o comportamento de um filtro RC passa-baixas no domínio da frequência.

O estudo envolve análise teórica, simulação computacional e validação experimental em laboratório.

🎯 Objetivos
Analisar a estabilidade do sistema
Obter a resposta em frequência (magnitude)
Determinar a frequência de corte
Verificar o comportamento do filtro com sinais senoidais
Comparar resultados teóricos e experimentais
⚙️ Parâmetros do Circuito
Resistência: 10 kΩ
Capacitância: 10 nF
Função de Transferência:
H(s)=
RCs+1
1
	​

Resposta em Frequência:
H(jω)=
1+jωRC
1
	​

📈 Resultados Teóricos
✔️ Estabilidade

O sistema é estável, pois seu polo está no semiplano esquerdo:

s=−
RC
1
	​

📉 Resposta em Magnitude
Baixas frequências → ganho ≈ 0 dB
Altas frequências → atenuação
Comportamento típico de filtro passa-baixas
🔥 Frequência de Corte
f
c
	​

=
2πRC
1
	​


Substituindo os valores:

f
c
	​

≈1,59 kHz
🧪 Experimento Prático
Sinal de Entrada:
v
i
	​

(t)=10cos(2π500t)+10cos(2π10000t)
500 Hz → baixa frequência
10 kHz → alta frequência
🔍 Observações

Antes do filtro:

Duas componentes presentes: 500 Hz e 10 kHz

Após o filtro:

500 Hz → praticamente mantida
10 kHz → fortemente atenuada

✔️ Resultado confirma o comportamento esperado de um filtro passa-baixas.

🛠️ Metodologia
Montagem do circuito em protoboard
Uso de:
Gerador de funções
Osciloscópio
Simulação da resposta em frequência utilizando Python

📊 Conclusão

O experimento demonstrou, de forma teórica e prática, que o filtro RC passa-baixas:

É estável
Atenua sinais de alta frequência
Permite a passagem de sinais de baixa frequência
Apresenta frequência de corte consistente com os cálculos

👨‍💻 Autores
João Vitor Moreno Matos
Eriklys Jonathan Gomes de Almeida
Maria Eduarda Abrantes da Silva

👨‍🏫 Professor

Pedro Thiago Valério de Souza

📚 Disciplina

Sinais e Sistemas

🚀 Como usar este projeto
Clone o repositório
Execute o código em Python (caso incluído)
Analise os gráficos gerados
Compare com os resultados experimentais
