from django.shortcuts import render
from images.models import LottiImage
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse, HttpRequest
from django.conf import settings

def index(request):
    image = LottiImage.objects.order_by('?').first()
    return render(request, 'images/index.html', {'image': image})


@user_passes_test(lambda u: u.is_staff)
def bulk(request):
    created = []
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
            try:
                created.append(LottiImage.objects.create(image=image))
            except:
                pass

    return render(request, 'images/bulk.html', {'created': created})


def random(request: HttpRequest):
    image = LottiImage.objects.order_by('?').values().first()
    image['image'] = request.build_absolute_uri(settings.MEDIA_URL + image['image'])
    return JsonResponse(image)
