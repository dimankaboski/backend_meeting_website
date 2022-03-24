from PIL import Image, ImageEnhance
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import logging


def add_watermark(image_url, watermark_url, opacity=1):
    image = Image.open(image_url)
    watermark = Image.open(watermark_url)
    assert opacity >= 0 and opacity <= 1
    if opacity < 1:
        if watermark.mode != 'RGBA':
            watermark = watermark.convert('RGBA')
        else:
            watermark = watermark.copy()
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
    layer = Image.new('RGBA', image.size, (0,0,0,0))
    layer.paste(watermark, (0, 0))
    image_ext = image_url.name.split('.')[-1]
    watermarked_image_url = f'{image_url.name}_marked.{image_ext}'
    Image.composite(layer,  image,  layer).save(settings.MEDIA_URL + watermarked_image_url)
    return watermarked_image_url