from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from django.http import Http404

# pictures/views.py
def picture_list(request):
    media_root = settings.MEDIA_ROOT
    media_url = settings.MEDIA_URL
    media_path = os.path.join(media_root, 'reservation_images')
    image_files = [
        {
            'id': i,
            'url': os.path.join(media_url, 'reservation_images', file),
        }
        for i, file in enumerate(os.listdir(media_path))
        if file.endswith(('.jpg', '.png', '.jpeg'))
    ]

    return render(request, 'pictures/picture_list.html', {'image_files': image_files})



def chosen_picture(request, image_id):
    image_files = [
        {
            'id': i,
            'url': os.path.join(settings.MEDIA_URL, 'reservation_images', file),
        }
        for i, file in enumerate(os.listdir(os.path.join(settings.MEDIA_ROOT, 'reservation_images')))
        if file.endswith(('.jpg', '.png', '.jpeg'))
    ]

    try:
        image = image_files[image_id]
    except IndexError:
        raise Http404("Image does not exist")

    return render(request, 'pictures/chosen_picture.html', {'image': image})