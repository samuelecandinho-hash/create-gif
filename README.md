# 🎞️ Create GIF com Python

Projeto desenvolvido em **Python** para criar arquivos **GIF a partir de imagens**, utilizando a biblioteca **ImageIO**.

O programa carrega imagens `.jpg` e utiliza essas imagens como quadros para gerar uma animação em formato `.gif`.

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🖼️ ImageIO

## 🎯 Objetivo

O objetivo deste projeto é aprender como criar um GIF utilizando imagens com Python.

O programa:

1. Define as imagens que serão utilizadas.
2. Carrega as imagens com o ImageIO.
3. Armazena as imagens em uma lista.
4. Cria um arquivo GIF.
5. Define o tempo de exibição de cada imagem.
6. Configura o GIF para repetir continuamente.


Após a execução, o arquivo `Natan.gif` será criado na mesma pasta do programa.

## 💻 Código

```python
import imageio.v3 as iio

arquivoImagens = ['normal.jpg', 'jumpcare.jpg']

Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))

iio.imwrite('Natan.gif', Imagens, duration=500, loop=0)
```

## 🔎 Como funciona

### Definição das imagens

```python
arquivoImagens = ['normal.jpg', 'jumpcare.jpg']
```

Define as imagens que serão utilizadas para criar o GIF.

### Carregamento das imagens

```python
Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))
```

O `for` percorre cada imagem definida em `arquivoImagens`.

A função `iio.imread()` realiza a leitura da imagem e adiciona o resultado à lista `Imagens`.

### Criação do GIF

```python
iio.imwrite('Natan.gif', Imagens, duration=500, loop=0)
```

O `iio.imwrite()` cria o arquivo GIF utilizando as imagens carregadas.

* `Natan.gif` → nome do arquivo gerado.
* `duration=500` → cada imagem é exibida por 500 milissegundos.
* `loop=0` → o GIF será reproduzido continuamente.

## 🖼️ Resultado

Ao executar o programa, será criado:

```text
Natan.gif
```

O GIF utiliza `normal.jpg` e `jumpcare.jpg` como quadros da animação.

## 📚 Aprendizados

Com este projeto, é possível praticar:

* Manipulação de imagens com Python;
* Leitura de arquivos `.jpg`;
* Utilização de listas;
* Estruturas de repetição;
* Uso de bibliotecas externas;
* Criação de arquivos `.gif`;
* Configuração de duração e repetição de animações.

## 👨‍💻 Autor

**Samuel**

Estudante de Desenvolvimento de Software, com interesse em programação, tecnologia e desenvolvimento de soluções.

---

⭐ Se este projeto foi útil, considere deixar uma estrela no repositório.
