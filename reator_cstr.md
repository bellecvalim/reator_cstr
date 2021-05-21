## Variáveis envolvidas no problema

* Vazão volumétrica do reagente <img src="https://render.githubusercontent.com/render/math?math=$A : q = 3 [L/s]$">
* Concentração do reagente <img src="https://render.githubusercontent.com/render/math?math=$A$"> na entrada: <img src="https://render.githubusercontent.com/render/math?math=$C_{a0} = 2 [mol/L]$">
* Volume do reator: <img src="https://render.githubusercontent.com/render/math?math=$V = 20 [L]$">
* Temperatura de entrada do reagente <img src="https://render.githubusercontent.com/render/math?math=$A: T_e = 350 [K]$">
* Massa específica do reagente <img src="https://render.githubusercontent.com/render/math?math=$A: \rho = 1000 [g/L]$">
* Calor específico do reagente <img src="https://render.githubusercontent.com/render/math?math=$A: C_p = 1.9 [J/g.K]$">
* Entalpia de reação: <img src="https://render.githubusercontent.com/render/math?math=$(-\Delta H_R) = 50000 [J/mol]$">
* Razão <img src="https://render.githubusercontent.com/render/math?math=$E/R = 8750 [K]$">
* Constante de velocidade: <img src="https://render.githubusercontent.com/render/math?math=$k_0 = 0.0029 [L/mol.min]$">
* Troca térmica <img src="https://render.githubusercontent.com/render/math?math=$UA = 50000 [J/min.K]$">
* Temperatura do fluido refrigerante: <img src="https://render.githubusercontent.com/render/math?math=$T_c = 100 [K]$">


## Condições iniciais adotadas

* Concentração inicial do reagente <img src="https://render.githubusercontent.com/render/math?math=$A: C_{a0} = 3.27 [mol/L]$">
* Temperatura inicial: <img src="https://render.githubusercontent.com/render/math?math=$T_0 = 250 [K]$">



## Considerações com relação ao sistema


* Consideramos a utilização de um reator CSTR encamisado. A reação é exotérmica e, por isso, precisamos da circulação de um líquido refrigerante para equilibrar a temperatura do sistema.

* A reação irreversível <img src="https://render.githubusercontent.com/render/math?math=$A \rightarrow B$"> ocorre em fase líquida.

* A cinética da reação é de primeira ordem (dada por <img src="https://render.githubusercontent.com/render/math?math=$-r_a = k.C_a$">), com relação ao reagente <img src="https://render.githubusercontent.com/render/math?math=$A$">.

* Como a constante cinética <img src="https://render.githubusercontent.com/render/math?math=$k$"> é influenciada pela temperatura, podemos escrevê-la como <img src="https://render.githubusercontent.com/render/math?math=$k=k_0.e^{(\frac{-E}{R.T})}$">.



## Considerações com relação ao modelo


* Mistura perfeita (<img src="https://render.githubusercontent.com/render/math?math=$C_a$"> não varia no espaço).

* Massa específica <img src="https://render.githubusercontent.com/render/math?math=$\rho$"> é constante.

* Volume do reator <img src="https://render.githubusercontent.com/render/math?math=$V$"> é constante. Logo, a vazão volumétrica <img src="https://render.githubusercontent.com/render/math?math=$q$"> de entrada, é igual à de saída.


## Modelagem matemática do sistema
### Balanço de massa

A massa é dada por <img src="https://render.githubusercontent.com/render/math?math=$m = \rho.V">. Para calcular a variação da massa ao longo do tempo, podemos fazer:

<img src="https://render.githubusercontent.com/render/math?math=$\frac{d(\rho.V)}{dt} = \rho. q_{ent} - \rho. q_{sai}$">

Como consideramos $\rho$ e $V$ constantes, temos que

<img src="https://render.githubusercontent.com/render/math?math=$q_{ent} - q_{sai} = 0$">


### Balanço de energia

Aqui precisamos fazer, ainda, mais algumas considerações.


* A temperatura do fluido refrigerante <img src="https://render.githubusercontent.com/render/math?math=$T_c$"> é constante.

* Calor retirado do sistema é <img src="https://render.githubusercontent.com/render/math?math=$Q = UA (T_c - T)$">. Consideramos como se fosse um trocador de calor.

* O sistema não realiza troca térmica com a vizinhança.


Dessa forma, temos que

<img src="https://render.githubusercontent.com/render/math?math=$\frac{(V.\rho.Cp)dT}{dt} = m.C_p.(T_e - T_{ref}) - m.Cp. (T - T_{ref}) + (-\Delta H_R).V.k.C_a + UA(T_c - T)$">

Simplificando,

<img src="https://render.githubusercontent.com/render/math?math=$\frac{(V.\rho.Cp)dT}{dt} = \rho.q.C_p.(T_e - T) + (-\Delta H_R).V.k.C_a + UA(T_c - T)$">

Como <img src="https://render.githubusercontent.com/render/math?math=$V$">, <img src="https://render.githubusercontent.com/render/math?math=$\rho$"> e <img src="https://render.githubusercontent.com/render/math?math=$C_p$"> são considerados constantes,

<img src="https://render.githubusercontent.com/render/math?math=$\frac{dT}{dt} = \frac{\rho.q.C_p.(T_e - T) + (-\Delta H_R).V.k.C_a + UA(T_c - T)}{V.\rho.C_p}$">


### Balanço por componente

Para o reagente <img src="https://render.githubusercontent.com/render/math?math=$A$">, temos que

<img src="https://render.githubusercontent.com/render/math?math=$\frac{dN_a}{dt} = N_{a(ent)} - N_a +V.k.C_a$">

Como <img src="https://render.githubusercontent.com/render/math?math=$N_a = V.C_a$">,

<img src="https://render.githubusercontent.com/render/math?math=$\frac{dVC_a}{dt} = q.(C_{a(ent)} - C_a) - V.k.C_a$">

Como <img src="https://render.githubusercontent.com/render/math?math=$V$"> é constante,

<img src="https://render.githubusercontent.com/render/math?math=$\frac{dC_a}{dt} = \frac{q.(C_{a(ent)} - C_a) - V.k.C_a}{V}$">