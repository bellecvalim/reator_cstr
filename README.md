## Variáveis envolvidas no problema


* Vazão volumétrica do reagente $A$: $q = 3 [L/s]$
* Concentração do reagente $A$ na entrada: $C_{a0} = 2 [mol/L]$
* Volume do reator: $V = 20 [L]$
* Temperatura de entrada do reagente $A$: $T_e = 350 [K]$
* Massa específica do reagente $A$: $\rho = 1000 [g/L]$
* Calor específico do reagente $A$: $C_p = 1.9 [J/g.K]$
* Entalpia de reação: $(-\Delta H_R) = 50000 [J/mol]$
* Razão $E/R = 8750 [K]$
* Constante de velocidade: $k_0 = 0.0029 [L/mol.min]$
* Troca térmica $UA = 50000 [J/min.K]$
* Temperatura do fluido refrigerante: $T_c = 100 [K]$


## Condições iniciais adotadas

* Concentração inicial do reagente $A$: $C_{a0} = 3.27 [mol/L]$
* Temperatura inicial: $T_0 = 250 [K]$



## Considerações com relação ao sistema


* Consideramos a utilização de um reator CSTR encamisado. A reação é exotérmica e, por isso, precisamos da circulação de um líquido refrigerante para equilibrar a temperatura do sistema.

* A reação irreversível $A$ $\rightarrow$ $B$ ocorre em fase líquida.

* A cinética da reação é de primeira ordem (dada por $-r_a = k.C_a$), com relação ao reagente $A$.

* Como a constante cinética $k$ é influenciada pela temperatura, podemos escrevê-la como $k=k_0.e^{(\frac{-E}{R.T})}$.



## Considerações com relação ao modelo


* Mistura perfeita ($C_a$ não varia no espaço).

* Massa específica $\rho$ é constante.

* Volume do reator $V$ é constante. Logo, a vazão volumétrica $q$ de entrada, é igual à de saída.


## Modelagem matemática do sistema
### Balanço de massa

A massa é dada por $m$ = \rho.V. Para calcular a variação da massa ao longo do tempo, podemos fazer:

$$
\frac{d(\rho.V)}{dt} = \rho. q_{ent} - \rho. q_{sai}
$$

Como consideramos $\rho$ e $V$ constantes, temos que

$$
q_{ent} - q_{sai} = 0
$$


### Balanço de energia

Aqui precisamos fazer, ainda, mais algumas considerações.


* A temperatura do fluido refrigerante $T_c$ é constante.

* Calor retirado do sistema é $Q = UA (T_c - T)$. Consideramos como se fosse um trocador de calor.

* O sistema não realiza troca térmica com a vizinhança.


Dessa forma, temos que

$$
\frac{(V.\rho.Cp)dT}{dt} = m.C_p.(T_e - T_{ref}) - m.Cp. (T - T_{ref}) + (-\Delta H_R).V.k.C_a + UA(T_c - T)
$$

Simplificando,

$$
\frac{(V.\rho.Cp)dT}{dt} = \rho.q.C_p.(T_e - T) + (-\Delta H_R).V.k.C_a + UA(T_c - T)
$$

Como $V$, $\rho$ e $C_p$ são considerados constantes,

$$
\frac{dT}{dt} = \frac{\rho.q.C_p.(T_e - T) + (-\Delta H_R).V.k.C_a + UA(T_c - T)}{V.\rho.C_p}
$$


### Balanço por componente

Para o reagente $A$, temos que

$$
\frac{dN_a}{dt} = N_{a(ent)} - N_a +V.k.C_a
$$

Como $N_a = V.C_a$,

$$
\frac{dVC_a}{dt} = q.(C_{a(ent)} - C_a) - V.k.C_a
$$

Como $V$ é constante,

$$
\frac{dC_a}{dt} = \frac{q.(C_{a(ent)} - C_a) - V.k.C_a}{V}
$$