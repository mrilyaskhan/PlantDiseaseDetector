from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadedImage
from .predict import predict_leaf_disease  # new import
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    images = UploadedImage.objects.filter(user=request.user).order_by('-id')
    return render(request, 'detector/dashboard.html', {'images': images})



@login_required
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            # --- AI prediction ---
            result, confidence = predict_leaf_disease(obj.image.path)
            obj.result = result
            obj.confidence = confidence
            obj.save()

            return redirect('detector:dashboard')
    else:
        form = UploadForm()
    return render(request, 'detector/upload.html', {'form': form})

@login_required
def delete_image(request, image_id):
    try:
        image = UploadedImage.objects.get(id=image_id, user=request.user)
        image.delete()
        messages.success(request, "Image deleted successfully!")
    except UploadedImage.DoesNotExist:
        messages.error(request, "Image not found or not yours.")

    return redirect('detector:dashboard')