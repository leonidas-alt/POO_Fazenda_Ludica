# 🐮 Fazenda Lúdica

Projeto desenvolvido como exercício de **Programação Orientada a Objetos (POO)** em Python, demonstrando os principais conceitos da orientação a objetos por meio de uma fazenda com diferentes tipos de animais.

---

## 📚 Conceitos aplicados

Neste projeto são utilizados diversos conceitos fundamentais da POO:

- ✅ Classes e Objetos
- ✅ Herança
- ✅ Polimorfismo
- ✅ Encapsulamento
- ✅ Construtores (`__init__`)
- ✅ Sobrescrita de métodos
- ✅ Uso de listas de objetos
- ✅ Verificação de tipos com `isinstance()`

---

## 📂 Estrutura do projeto

```
Fazenda Ludica/
│
├── main.py
└── README.md
```

---

## 🐾 Classes implementadas

### Animal

Classe base responsável por representar qualquer animal da fazenda.

**Atributos**

- `nome`
- `idade`

**Métodos**

- `apresentar()`
- `emitir_som()`

---

### Cachorro

Classe que herda de `Animal`.

**Atributos**

- `raça`

**Comportamento**

Sobrescreve o método `emitir_som()` retornando:

```
Au! Au!
```

---

### Gato

Classe derivada de `Animal`.

**Atributos**

- `cor_pelo`

**Comportamento**

Sobrescreve o método `emitir_som()` retornando:

```
Miau!
```

---

### Vaca

Classe derivada de `Animal`.

**Atributos**

- `__producao_leite_litros` *(privado)*

**Métodos**

- `emitir_som()`
- `obter_producao_leite()`
- `registrar_ordenha()`

O atributo da produção de leite utiliza **encapsulamento**, permitindo acesso apenas através de métodos específicos.

---

## 🔄 Polimorfismo

Todos os animais possuem o método `emitir_som()`, porém cada classe implementa seu próprio comportamento.

Exemplo:

| Animal | Som |
|---------|-----|
| Cachorro | Au! Au! |
| Gato | Miau! |
| Vaca | Muuu! |

---

## ▶️ Funcionamento

São criados três objetos:

- 🐶 Rex
- 🐱 Mimi
- 🐮 Mimosa

Todos são armazenados em uma lista.

Em seguida, um laço percorre essa lista chamando os métodos de cada objeto, demonstrando o polimorfismo.

Além disso, utilizando `isinstance()`, o programa identifica o tipo do animal para exibir suas características específicas.

---

## 💻 Exemplo de saída

```text
Olá, sou Rex e tenho 3
Au! Au!
Minha raça é: Labrador

Olá, sou Mimi e tenho 5
Miau!
Meu pelo é: Branco

Olá, sou Mimosa e tenho 7
Muuu!
Minha produção de leite é: 25.5
```

---

## 🚀 Tecnologias

- Python 3

---

## 📖 Objetivo acadêmico

Este exercício tem como objetivo praticar os pilares da Programação Orientada a Objetos, reforçando conceitos como:

- Herança entre classes
- Reutilização de código
- Polimorfismo
- Encapsulamento
- Manipulação de objetos
- Organização de código utilizando classes

---

## ⚠️ Observação

O código original possui alguns pequenos erros de sintaxe na parte final:

```python
if isinstance(animal.Gato):
```

O correto é:

```python
if isinstance(animal, Gato):
```

Da mesma forma:

```python
if isinstance(animal.Vaca):
```

deve ser:

```python
if isinstance(animal, Vaca):
```

Também é possível remover os `print()` envolvendo `animal.apresentar()`, já que esse método já realiza a impressão da mensagem.

---

### 👨‍💻 Autor

Exercício desenvolvido para estudos de **Programação Orientada a Objetos (POO)** utilizando Python.
