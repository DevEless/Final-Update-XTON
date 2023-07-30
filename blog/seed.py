from django_seed import Seed
from .models import CategoryArticle, Tag, Article
from user.models import User


def runBlog():
    seeder = Seed.seeder()

    # Création des catégories pour les voitures
    categories = [ "Sedan", "Sport", "Électrique"]
    for category in categories:
        CategoryArticle.objects.create(category=category)

    # Création des tags liés aux voitures
    tags = ["Puissance", "Design", "Luxueux", "Écologique", "Vitesse", "Conduite", "Innovation", "Performance"]
    for tag in tags:
        Tag.objects.create(tag=tag) 


    articles = [
        {
            "title": "Tesla Model S",
            "img": "https://th.bing.com/th/id/R.25112fabec00618a9cf5d9e73d5ad9b4?rik=Lrazy9yg1wZ%2bgw&pid=ImgRaw&r=0",
            "description": "La Tesla Model S est une berline électrique de luxe aux performances exceptionnelles.",
            "category": CategoryArticle.objects.get(category="Sedan"),
            "tag": Tag.objects.filter(tag__in=["Électrique", "Luxueux", "Innovation"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Porsche 911",
            "img": "https://th.bing.com/th/id/R.fdf140be0c5d82cce6e5ce72c341ed57?rik=NxNs%2bJ6MmN%2fR9w&pid=ImgRaw&r=0",
            "description": "La Porsche 911 est un modèle emblématique de voiture de sport avec un design élégant et des performances de haut niveau.",
            "category": CategoryArticle.objects.get(category="Sport"),
            "tag": Tag.objects.filter(tag__in=["Sport", "Vitesse", "Performance"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "BMW i8",
            "img": "https://th.bing.com/th/id/R.0e2057ae3a6dfac19f5d9280a8a56f81?rik=6mY%2fq0IHHZBP0A&riu=http%3a%2f%2fwww.automotiveaddicts.com%2fwp-content%2fuploads%2f2013%2f09%2fbmw-i8-1.jpg&ehk=W7Nk4HhueLwrpd%2b73%2bE2BK8Vjh2XWckL%2fZToY8NCGPs%3d&risl=&pid=ImgRaw&r=0",
            "description": "La BMW i8 est une voiture hybride rechargeable au design futuriste et aux performances équilibrées.",
            "category": CategoryArticle.objects.get(category="Sport"),
            "tag": Tag.objects.filter(tag__in=["Écologique", "Design", "Puissance"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Mercedes-Benz GLE",
            "img": "https://th.bing.com/th/id/R.707ff99b8c29d3b09cc410f0bfe79e9d?rik=pWnit%2bF0VqcCVw&riu=http%3a%2f%2fsax4x4.s3-eu-west-1.amazonaws.com%2fWDC2923242A036121%2f360doorsclosed%2fXC_WDC2923242A036121_BT66UJW_01.jpg&ehk=hJGtS1hVjvRkHB7HY2P4JO7qmQxm3spyRVImXqi0ecA%3d&risl=&pid=ImgRaw&r=0",
            "description": "Le Mercedes-Benz GLE est un SUV de luxe offrant un mélange parfait de confort et de performances.",
            "category": CategoryArticle.objects.get(category="Sedan"),
            "tag": Tag.objects.filter(tag__in=["Luxueux", "Conduite", "Design"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Ferrari LaFerrari",
            "img": "https://th.bing.com/th/id/OIP.HaTJ1pSeEuu0LBqgRTAZWQHaEK?pid=ImgDet&rs=1",
            "description": "La Ferrari LaFerrari est une supercar hybride avec un design époustouflant et des performances inégalées.",
            "category": CategoryArticle.objects.get(category="Sport"),
            "tag": Tag.objects.filter(tag__in=["Puissance", "Vitesse", "Performance"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Audi A7",
            "img": "https://th.bing.com/th/id/OIP.2Q2VjU0f_6zH8d7T5vuSmgHaEK?pid=ImgDet&rs=1",
            "description": "L'Audi A7 est une berline de luxe avec un design élégant et des technologies innovantes.",
            "category": CategoryArticle.objects.get(category="Sedan"),
            "tag": Tag.objects.filter(tag__in=["Luxueux", "Conduite", "Innovation"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Lamborghini Huracán",
            "img": "https://www.hdcarwallpapers.com/walls/vf_engineering_lamborghini_huracan_performante_2020_4k-HD.jpg",
            "description": "La Lamborghini Huracán est une supercar avec un moteur V10 rugissant et un design audacieux.",
            "category": CategoryArticle.objects.get(category="Sport"),
            "tag": Tag.objects.filter(tag__in=["Sport", "Vitesse", "Performance"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Nissan Leaf",
            "img": "https://electrek.co/wp-content/uploads/sites/3/2014/04/2014_nissan_leaf_25.jpg",
            "description": "La Nissan Leaf est une voiture électrique abordable et écologique, idéale pour une conduite urbaine.",
            "category": CategoryArticle.objects.get(category="Électrique"),
            "tag": Tag.objects.filter(tag__in=["Écologique", "Innovation", "Conduite"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
    ]


    for art in articles:
        category_name = art["category"]
        category, created = CategoryArticle.objects.get_or_create(category=category_name)
        # La méthode get_or_create récupère la catégorie s'il existe, sinon la crée.

        article = Article.objects.create(
            title=art["title"],
            img=art["img"],
            description=art["description"],
            category=category,
            user=art["user"],
            validate=art["validate"],
        )
        article.tag.set(art["tag"])

    print("Seeding completed successfully!")

runBlog()
