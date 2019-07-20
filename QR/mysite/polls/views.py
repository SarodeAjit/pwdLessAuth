# from wagtail.images.models import Image as WagtailImage
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .forms import *
import random

import qrcode
from django.conf import settings 
from django.conf.urls.static import static 
import base64
from io import StringIO, BytesIO
from PIL import Image

# from django.urls import reverse


# from wagtail.images.views.serve import generate_signature

def index(request):
    latest_question_list = 0
    if 'uniqeId' in request.session:
        latest_question_list = request.session['uniqeId']
        print("from session")
    else:
        latest_question_list = random.randint(1,1000001)
        request.session['uniqeId'] = latest_question_list
        print("new session")
    
    print("sessionId:" + str(latest_question_list))
    
    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    # The data that you want to store
    data = "192.168.0.111/" + str(latest_question_list)

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    name = "img" +  str(latest_question_list) + ".png"
    img_dst =   settings.MEDIA_ROOT  +"/"   + name
    print("storage" + img_dst)
    img.save(img_dst)
 

    cQrCodesObj = cQrCode()
    cQrCodesObj.uniqueId = str(latest_question_list)
    cQrCodesObj.QrCodeImg_name = name
    print(cQrCodesObj.uniqueId)
    print(cQrCodesObj.QrCodeImg_name)
    return render(request, 'polls/index.html',  {'cQrCodes_image' : cQrCodesObj} )


 
