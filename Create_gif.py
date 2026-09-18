import  imageio.v3 as iio


arquivoImagens = ['normal.jpg', 'jumpcare.jpg']
Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))

iio.imwrite('Natan.gif', Imagens, duration = 500, loop = 0)