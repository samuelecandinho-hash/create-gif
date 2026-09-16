import  imageio.v3 as iio


arquivoImagens = ['Create_gif/normal.jpg', 'Create_gif/jumpcare.jpg']
Imagens = []

for arquivoImagem in arquivoImagens:
    Imagens.append(iio.imread(arquivoImagem))

iio.imwrite('Create_gif/Natan.gif', Imagens, duration = 500, loop = 0)