"""
lists, Tuples, Str -> Sequences -> Iteráveis
---------------------------------
GERADORES:
Para criar um Generator basta definir uma função e utilizar a
palavra reservada yield , ao invés de return
--------------------------

###################  O protocolo Iterator  ################

O protocolo Iterator facilita muito a criação de um objeto iterável.

Para criá-lo, codificamos uma classe e basta que ela implemente os seguintes métodos:

__iter__: Esse métodos deve retornar o próprio objeto (self) para ser utilizado em
loops com for e in.
__next__: Esse método deve retornar o próximo valor da iteração. Caso a condição de
para seja satisfeita, ou seja, quando não houver mais objetos a iterar, ela deve
lançar o erro StopIteration.Python sempre simples! :wink:

Vamos criar um exemplo.

Vamos criar uma classe que nos permita iterar sobre a sequência de Fibonacci.

Relembrando: A sequência de Fibonacci é uma sequência de números inteiros onde um
número, após os dois primeiros números (que são 0 e 1), é a soma dos últimos dois.
Assim:

0, 1, 1, 2, 3, 5, 8, 13, 21,…

Com isso, e sabendo que devemos criar os métodos __iter__ e __next__, podemos
codificá-lo da seguinte forma:

class Fibonacci:
  def __init__(self, maximo=1000000):
    # Inicializa os dois primeiros numeros
    self.elemento_atual, self.proximo_elemento = 0, 1
    self.maximo = maximo

  def __iter__(self):
    # Retorna o objeto iterável (ele próprio: self)
    return self

  def __next__(self):
    # Fim da iteração, raise StopIteration
    if self.elemento_atual > self.maximo:
      raise StopIteration

    # Salva o valor a ser retornado
    valor_de_retorno = self.elemento_atual

    # Atualiza o próximo elemento da sequencia
    self.elemento_atual, self.proximo_elemento = self.proximo_elemento, self.elemento_atual + self.proximo_elemento

    return valor_de_retorno

# Executa nosso código
if __name__ == '__main__':
  # Cria nosso objeto iterável
  objeto_fibonacci = Fibonacci(maximo=1000000)

  # Itera nossa sequencia
  for fibonacci in objeto_fibonacci:
    print("Sequencia: {}".format(fibonacci))

No código acima:

Inicializamos o elemento atual, o próximo elemento e o valor máximo da nossa
sequência no construtor __init__.

Retornamos self no método __iter__, conforme citado lá em cima.
No método __next__, primeiro verificamos se a condição de parada foi satisfeita
(caso positivo, lançamos a exceção StopIteration). Em seguida, atualizamos os
valores atual e próximo para iteração seguinte, e retornamos o valor de retorno
da iteração atual.

Vejam a simplicidade do Python.

Diferente do Java ou outras linguagens, onde temos que herdar uma classe ou
implementar uma interface, tornando nosso código muito mais extenso e verboso,
em Python, basta definir o comportamento (__iter__ e __next__) que a linguagem
já entende que estamos implementando o protocolo Iterator.

Mágico né?!

Com isso, podemos passar para a melhor parte: os Generators!

################   Generator   #################

O conceito de Generator em Python, criado pela PEP 255, é uma forma mais simples e
rápida de se implementar o protocolo Iterator, pois não necessita a criação de uma
classe para tal.

Para criar um Generator basta definir uma função e utilizar a palavra reservada
yield, ao invés de return.

Vamos ver como criar a nossa sequência de Fibonnaci, mas agora utilizando o conceito
 de Generator:

def fibonacci(maximo):
  # Inicialização dos elementos
  elemento_atual, proximo_elemento = 0, 1

  # Defina a condição de parada
  while elemento_atual < maximo:
    # Retorna o valor do elemento atual
    yield elemento_atual

    elemento_atual, proximo_elemento = \
        proximo_elemento, elemento_atual + proximo_elemento

if __name__ == '__main__':
  # Cria um generator de números fibonacci menor que 1 milhão
  fibonacci_generator = fibonacci(1000000)

  # Mostra na tela toda a sequencia
  for numero_fibonacci in fibonacci_generator:
    print(numero_fibonacci)

Vamos entender melhor o fluxo de execução para fixar o entendimento:

Na primeira chamada à nossa função fibonacci(), o Python vai executar da linha 1 à
linha 8 com elemento_atual = 0 e proximo_elemento = 1.
Como o generator salva o estado da função no momento do retorno (yield), a segunda
execução não começará na linha 1, mas sim na linha subsequente ao yield, ou seja, a
partir da linha 10. Em seguida continua a repetição dentro do while (linha 6), mas
agora com o valor atualizado de elemento_atual, retorna em yield` e assim sucessivamente.
Diferente da implementação por classe, onde tivemos que lançar um erro StopIteration
 para sinalizar o fim da iteração, aqui o fim da execução é sinalizado, apenas, por
não retornar um valor. Ou seja, a primeira vez que o código do nosso generator não
retornar um valor, o Python entende que esse é o fim da iteração e finaliza o for/in
da linha 18.

Ficou claro? Entender esse fluxo é MUITO importante! Qualquer dúvida, não hesite em
 postar no box de comentários aqui embaixo!

##############  Lazy Evaluation  ###############

Outro ponto importante para se ressaltar aqui, é o conceito de lazy evaluation
(“avaliação preguiçosa” em português).

Iterators e Generators não computam todos os valores do seu loop quando são criados
ou instanciados.

Eles computam sob demanda, isto é: APENAS quando pedimos o próximo valor da sequência.

Nos exemplos acima (com a classe Fibonacci e com a função fibonacci()), o Python não
calculou a sequência inteira até o milionésimo número (maximo=1000000), no momento de
sua criação.

O que ele fez foi calcular o primeiro número da sequência, aguardar o próximo ciclo
do loop, calcular o segundo número, aguardar o próximo ciclo e assim sucessivamente,
até que a condição de parada (elemento_atual < maximo) fosse alcançada.

Portanto, a cada iteração do loop nas linhas 19 e 20, nosso generator gera apenas um
novo número, utilizando o passado e o atual, salvando assim, a preciosa memória da sua
máquina.

Uma forma de se percebir isso, é chamando a função next() do próprio Python (built-in)
diversas vezes.

Essa função traz o próximo item do objeto iterável. Por exemplo:

# Cria um generator de números fibonacci menor que mil
fibonacci_generator = fibonacci(1000)

next(fibonacci_generator)
next(fibonacci_generator)
next(fibonacci_generator)
next(fibonacci_generator)

Gera a seguinte saída:
0
1
1
2

Observação: Não tente reutilizar o generator após iterar sobre ele. Um generator só
pode ser consumido uma única vez. Para utilizá-lo novamente, é necessário criá-lo ou
instanciá-lo novamente.

####################   Generators e Listas ####################

Listas podem ser criadas através de objetos iteravéis.

Por exemplo, como range é iterável, o código: list(range(5)) gera a seguinte saída:
[0, 1, 2, 3, 4]

Como um generator também é iterável, o código list(fibonacci(1000)) gera (adivinha)
a seguinte saída:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

Melhor ainda, utilizando List Comprehensions (assunto para um próximo post), podemos
 fazer, por exemplo:

fibonacci_impares = [x for x in fibonacci(100000) if x%2 != 0]
print("Número ímpares são: {0}".format(fibonacci_impares))

Número ímpares são: [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987]


Conclusão
Nesse post, quis demonstrar um pouco do potencial dos Iterators e Generators e como são simples de serem utilizados!

Vimos que generators otimizam a utilização de memória, pois não guardam grandes estruturas na memória da sua máquina.

Agora…

Que tal dar uma revisitada nos seus códigos, focando naqueles loops imensos?

Talvez ali haja uma boa oportunidade de botar em prática a teoria que você leu aqui!

Bom desenvolvimento!

"""


# Iteráveis
nome = 'Luiz Otávio'
# Iterador
iterador = iter(nome) # transforma o iterável em iterardor
# Gerador
gerador = (letra for letra in nome) # geradores são "list comprehension" com parênteses()


print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('OLHA O FOR')
for letra in gerador:
    print(letra)

print('OLHA O OUTRO FOR')
for letra in gerador:
    print(letra)

print(next(gerador))


# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)