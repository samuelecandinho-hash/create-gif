# 🎞️ Create GIF com Python

Projeto desenvolvido em **Python** para criar arquivos **GIF a partir de imagens**, utilizando a biblioteca **ImageIO**.

O projeto demonstra como carregar múltiplas imagens, armazená-las em uma lista e gerar um GIF com duração definida para cada quadro.

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🖼️ ImageIO

## 🎯 Objetivo

O objetivo deste projeto é demonstrar como criar um GIF utilizando imagens como quadros de uma animação.

O programa:

1. Define os caminhos das imagens.
2. Carrega cada imagem utilizando o ImageIO.
3. Armazena as imagens em uma lista.
4. Gera um arquivo `.gif`.
5. Define a duração de cada imagem.
6. Configura o GIF para repetir continuamente.

## 📂 Estrutura do projeto

```text
create-gif-com-python/
│
├── Create_gif/
│   ├── normal.jpg
│   ├── jumpcare.jpg
│   └── Natan.gif
│
├── main.py
└── README.md
```

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/samuelecandinho-hash/create-gif-com-python.git
```

### 2. Acesse a pasta do projeto

```bash
cd create-gif-com-python
```

### 3. Instale o ImageIO

```bash
pip install imageio
```

## ▶️ Execução

Após instalar as dependências, execute o arquivo Python:

```bash
python main.py
```

O programa irá carregar as imagens presentes na pasta `Create_gif` e gerar o arquivo GIF.

## 💻 Código

```python
import imageio.v3 as iio

arquivoImagens = [
    'Create_gif/normal.jpg',
    'Create_gif/jumpcare.jpg'
]

Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))

iio.imwrite(
    'Create_gif/Natan.gif',
    Imagens,
    duration=500,
    loop=0
)
```

## 🔎 Como funciona

### Importação do ImageIO

```python
import imageio.v3 as iio
```

Importa o módulo `imageio.v3`, utilizado para leitura e escrita de arquivos de imagem.

### Definição das imagens

```python
arquivoImagens = [
    'Create_gif/normal.jpg',
    'Create_gif/jumpcare.jpg'
]
```

Define os caminhos das imagens que serão utilizadas na criação do GIF.

### Carregamento das imagens

```python
Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))
```

O programa percorre os arquivos definidos e utiliza `iio.imread()` para carregar cada imagem. As imagens são armazenadas na lista `Imagens`.

### Criação do GIF

```python
iio.imwrite(
    'Create_gif/Natan.gif',
    Imagens,
    duration=500,
    loop=0
)
```

O método `iio.imwrite()` cria o arquivo GIF utilizando as imagens carregadas.

* `Natan.gif`: nome do arquivo de saída.
* `duration=500`: cada imagem permanece durante 500 milissegundos.
* `loop=0`: faz o GIF repetir continuamente.

## 🖼️ Resultado

Após a execução, será criado o arquivo:

```text
Create_gif/Natan.gif
```

O arquivo contém as imagens utilizadas pelo programa organizadas como uma animação GIF.

## 📚 Aprendizados

Este projeto permite praticar:

* Manipulação de imagens com Python;
* Leitura de arquivos de imagem;
* Utilização de listas;
* Estruturas de repetição;
* Instalação e utilização de bibliotecas externas;
* Criação de arquivos GIF;
* Configuração de duração e repetição de animações.

## 👨‍💻 Autor

**Samuel**

Estudante de Desenvolvimento de Software, com interesse em programação, tecnologia e desenvolvimento de soluções.

🔗 **GitHub:**
https://github.com/samuelecandinho-hash

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório.
