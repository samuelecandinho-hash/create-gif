import  imageio.v3 as iio


arquivoImagens = ['jumpcare.jpg', 'normal.jpg']
Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))

iio.imwrite('Natan.gif', Imagens, duration = 500, loop = 0)