#1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado 
#“calcular_area” que retorna a área do círculo.

class Circulo:
    def _init_(self, raio):
        self.raio = raio
    def calcular_area(self):
        return 3.14159 * self.raio ** 2
    
#2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método 
#chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f'Título: {self.titulo}, Autor: {self.autor}'

#3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método 
#chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

#4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente 
#métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def _init_(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

#5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método 
#chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"{self.nome} diz: Olá!")

#6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um 
#método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def _init_(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

#7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método 
#chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def _init_(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'

#8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado 
#“calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def _init_(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

#9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um 
#método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def _init_(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

#10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um 
#método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário 
#do funcionário.

class Funcionario:
    def _init_(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual / 100)