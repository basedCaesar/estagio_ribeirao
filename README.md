# Questões Estágio Target Sistemas:
**1.**  Observe o trecho de código abaixo:
```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

```
Ao final do processamento, qual será o valor da variável SOMA?

**Resposta:**
O valor da soma será 91, confira a resolução [aqui](ex1.py).

---

**2.**  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

**Resposta:**
Confira a resolução [aqui](ex2.py).

---

**3.**  Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, **9**

b) 2, 4, 8, 16, 32, 64, **128**

c) 0, 1, 4, 9, 16, 25, 36, **49**

d) 4, 16, 36, 64, **100**

e) 1, 1, 2, 3, 5, 8, **13**

f) 2,10, 12, 16, 17, 18, 19, **200**

---

**4.**  Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

**Resposta:**

  - **_Passo 1:_** Ligue um  interruptor qualquer e espere alguns minutos
  - **_Passo 2:_** Desligue o interruptor e ligue um que não foi acionado ainda.
  - **_Passo 3:_** Vá à uma das salas e verifique o estado da lâmpada, Se ela estiver acessa, então ela corresponde ao interruptor acionado no passo 2, caso ela esteja apagada, mas quente ao toque, ela corresponde ao interruptor acionado no passo 1, e caso ela esteja apagada e fria, corresponde ao interruptor não ainda acionado.
  - **_Passo 4:_** Tendo determinado o interruptor da sala anterior, vá para outra sala, realize o mesmo processo excluindo o interruptor já determinado, assim você descobrirá o interruptor correspondente a essa sala e por exclusão o interruptor da sala restante.

---

**5.** Escreva um programa que inverta os caracteres de um string.

**IMPORTANTE:**

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

**Resposta:**
Confira a resolução [aqui](ex3.py).
