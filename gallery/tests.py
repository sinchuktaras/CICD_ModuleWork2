from django.test import TestCase
from django.urls import reverse
from .models import Image
from django.utils import timezone

class ImageModelTest(TestCase):
    def test_create_image(self):
        image = Image.objects.create(
            title='Test Image',
            description='A test image',
            image='gallery/test.jpg',
            created_date=timezone.now()
        )
        self.assertEqual(str(image), 'Test Image')

class GalleryViewTest(TestCase):
    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('gallery_view'))
        self.assertEqual(response.status_code, 200)

class ImageDetailViewTest(TestCase):
    def test_image_detail_view(self):
        image = Image.objects.create(
            title='Detail Image',
            description='Detail',
            image='gallery/test.jpg',
            created_date=timezone.now()
        )
        response = self.client.get(reverse('image_detail', args=[image.id]))
        self.assertEqual(response.status_code, 200)



