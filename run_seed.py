import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projet_Final.settings')
django.setup()

from user.seed import runConnexion
from product.seed import runProduct
from blog.seed import runBlog
from contact.seed import runContact


if __name__ == '__main__':
    runConnexion()
    runProduct()
    runBlog()
    runContact()
