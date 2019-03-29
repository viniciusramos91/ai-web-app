from django.shortcuts import render
from fastai import *
from fastai.vision import *
from django.http import HttpRequest, HttpResponse
from io import BytesIO


# View da página principal

def index(request: HttpRequest) -> HttpResponse:

    # Verifica o método HTTP
    if request.method == 'GET':
        # Se GET, renderiza a página HTML
        return render(request, 'webapp/index.html', status=200)
    
    # Se POST
    elif request.method == 'POST':
        # Pega a image da requisição
        image = request.FILES['image']

        # Lê os bytes da imagem
        data = BytesIO(image.read())

        # Chama o PIL para converter a imagem em preto e branco
        img = PIL.Image.open(data).convert('LA')

        # Salva a imagem em disco
        img.save('imagem.png')

        # Abre a imagem com o fast.ai
        img = open_image('imagem.png')

        # Carrega o conjunto padrão de transformações do fast.ai para aplicar na imagem
        tfms = get_transforms()

        # Aplica as transofmrações na imagem
        for transformation in tfms:
            fastai_img = img.apply_tfms(transformation, size=224)

        # Carrega o modelo
        learn = load_learner('/home/jupyter/playground', fname='modelo.pkl')

        # Executa o modelo sobre a imagem
        pred_class, pred_idx, outputs = learn.predict(fastai_img)

        return render(request, 'webapp/result.html', {'result': pred_class}, status=200)

    else:
        return HttpResponse('Método não permitido', status=405)

