

from django.shortcuts import render
from .forms import QRCodeForm
import os
from django.conf import settings

import qrcode

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            #to gengerate QR code you need  to install the package go to python qrcode library
            #install qrcode package
            #also install pillow will take your url and create qrcode for you and it will store it in png format
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "-").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) #media/11floor_restaurant_menu.png
            qr.save(file_path)
            

            #create image url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            #we want to print the restaurant name in the frontend
            context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            #once qr code is generated will return the to the result page we want this qr code to be downloadable
            return render(request, 'qr_result.html', context)

        return

    else:
        form = QRCodeForm()
        context = {
            'form': form,
        }
        return render(request, "generate_qr_code.html", context)