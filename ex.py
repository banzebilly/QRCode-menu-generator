from django.shortcuts import render
from .forms import QRCodeForm
import os
from django.conf import settings

import qrcode

def generate_qr_code(request):

    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name= form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            qr = qrcode.make(url)
            file_name = res_name.replace(' ', '-').lower() + 'menu.png'

            file_path = os.path.join(settings.MEDIA_ROOT, file_name)

            qr.save(file_path )
