# from wagtail.images.models import Image as WagtailImage
from django.shortcuts import render, redirect, render_to_response
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
from django.core.exceptions import ObjectDoesNotExist

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
    data = "192.168.0.111:8999/" + str(latest_question_list)

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
 
    # try to fetch data from DB
    try:
        cQrCodesExisting = cQrCode.objects.get(uniqueId=int(latest_question_list))
        #no exception means object preesent and can be filtered against auth to redirect to Welcome Page
        if cQrCodesExisting.isAuthenticated == True : 
            print ("auth Done")
            # return redirect('success/')
            return render_to_response( 'polls/welcome.html'  )
    except ObjectDoesNotExist:
        print("do nothing for now")
            

    cQrCodesObj = cQrCode()
    cQrCodesObj.uniqueId = int(latest_question_list)
    cQrCodesObj.QrCodeImg_name = name
    cQrCodesObj.isAuthenticated = False
    try:
        cQrCodesObj.save()
    except:
        print("Do nothing")
        
    print("saving object to DB")
    print(cQrCodesObj.uniqueId)
    print(cQrCodesObj.QrCodeImg_name)
    return render(request, 'polls/index.html',  {'cQrCodes_image' : cQrCodesObj} )

def update(request):
    print("refresh on same page is generated")
    return render(request, 'polls/index.html',  {'cQrCodes_image' : cQrCodesObj} )
 
def success(request):
    return render(request, 'polls/welcome.html'  )
