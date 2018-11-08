from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
import pymongo
import json
import os
import time
from .models import Folder, ImageModel

# client = pymongo.MongoClient('127.0.0.1', 27017)
# folder_collection = client['mzitu']['images']


def get_folder_name(path):
    return path[path.rindex('\\') + 1:len(path)]


# Create your views here.
# def handler(request):
#     start = time.time()
#     img_folder = 'D:\\mzitu\\full'
#     g = os.walk(img_folder)
#     id = 0
#     for path, dir_list, file_list in g:
#         folder = Folder(
#             id=id,
#             name=get_folder_name(path),
#             path=path,
#             file_count=len(os.listdir(path)))
#         folder.save()
#         id = id + 1
#     spend_time = time.time() - start
#     return HttpResponse(request, "Succeed {time}".format(time=spend_time))


def handler(request):
    # folders = Folder.objects.all()
    # for folder in folders:
    #     for file in os.listdir(folder.path):
    #         image = ImageModel(
    #             name=file,
    #             path=folder.path + "/" + file,
    #             size=os.path.getsize(folder.path + "/" + file),
    #             folder=folder)
    #         image.save()
    return HttpResponse("Succeed")


def index(request):
    folders = Folder.objects.order_by('-file_count')[:20]
    return render(request, 'image/index.html', context={'folders': folders})


def folder_detail(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    files = folder.imagemodel_set.all()
    return render(
        request,
        'image/folder.html',
        context={
            'image_name': folder.name,
            'images': files
        })


def image_detail(request, image_id):
    image = ImageModel.objects.get(id=image_id)
    return render(request, 'image/images.html', context={'image': image})