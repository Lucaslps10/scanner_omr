# View que processa o upload e chama o OMR

from django.shortcuts import render

# Create your views here.

import os
from .forms import UploadImageForm
from django.conf import settings
from omr.omr_scanner import OMRScanner
from .models import UploadOMR


# Chave de respostas fixa (você pode depois tornar dinâmica)
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

def upload_image(request):
    score = None
    image_url = None

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_file = form.cleaned_data['image']
            
            # Salva a imagem temporariamente
            save_path = os.path.join(settings.MEDIA_ROOT, 'respostas', image_file.name)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # Executa o scanner
            scanner = OMRScanner(save_path, ANSWER_KEY)
            scanner.scan()

            # Salva imagem corrigida
            result_image = scanner.get_result_image()
            result_path = os.path.join(settings.MEDIA_ROOT, 'resultados', image_file.name)
            os.makedirs(os.path.dirname(result_path), exist_ok=True)
            import cv2
            cv2.imwrite(result_path, result_image)

            # Caminho para exibir no template
            image_url = settings.MEDIA_URL + 'resultados/' + image_file.name
            score = round(scanner.score, 2)

            # Salva no banco de dados
            UploadOMR.objects.create(imagem='resultados/' + image_file.name, nota=score)

    else:
        form = UploadImageForm()
        

    return render(request, 'omr_web/upload.html', {
        'form': form,
        'score': score,
        'image_url': image_url,
    })
