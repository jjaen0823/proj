from django.db import models
from imagekit.models import ImageSpecField  # 썸네일을 만드는 작업의 중추를 하는 함수
                                          # source='image' 로 어떤 이미지를 리소스로 사용할지 설정하고, processors 에 여러 항목들을 추가해 썸네일을 제어
from imagekit.processors import ResizeToFill  # ResizeToFill(120,100) 은 썸네일의 크기를 조절
                                        # format 은 파일의 확장자, options는 파일의 압축방식을 의미

class Blog(models.Model):
    text = models.TextField()

# Create your models here.
class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='blogimg')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120,100)], format='JPEG', options={'quality': 60})