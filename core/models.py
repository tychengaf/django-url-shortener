import random
import string
from django.db import models

HASH_LENGTH = 8

def get_random_alphanumeric_string():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(HASH_LENGTH)))
    
   

class Url(models.Model):

    shorten_hash = models.CharField(primary_key=True, unique=True, default=get_random_alphanumeric_string, max_length=HASH_LENGTH)
    target_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        if not self.target_url:
            return f'empty -> domain/{self.shorten_hash}'
        return f'{self.target_url} -> domain/{self.shorten_hash}'
