from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import UploadedImage
from .forms import ImageUploadForm
from fpdf import FPDF
import os
from django.conf import settings

def convert_image_to_pdf(image, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image.image.path, x=10, y=10, w=190)
    pdf.output(pdf_path)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()

            # Define PDF path and convert image to PDF
            pdf_path = os.path.splitext(image.image.path)[0] + '.pdf'
            convert_image_to_pdf(image, pdf_path)

            # Update the 'pdf' field in the model
            image.pdf = pdf_path
            image.save()

            return redirect('image_list')

    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_list.html', {'images': images})
