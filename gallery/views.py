from django.shortcuts import render, get_object_or_404
from .models import Image
from django.utils import timezone
from datetime import timedelta

def gallery_view(request):
    month_ago = timezone.now() - timedelta(days=30)
    images = Image.objects.filter(created_at__gte=month_ago)
    return render(request, 'gallery.html', {'images': images})

def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'image_detail.html', {'image': image})