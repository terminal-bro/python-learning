from django.db import models
import random
import string 

# Create your models here.

def generate_shortcode(length = 6):
    characters  = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if not URLMap.objects.exists.filter(short_code=short_code).exists():
            return short_code

class URLMap(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True, blank= True)
    created_at = models.DateTimeField(auto_now_add= True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_shortcode()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.short_code} -> {self.original_url} '
    
    def get_shortened_url(self, request):
        return request.build_absolute_uri(f's/{self.short_code}')