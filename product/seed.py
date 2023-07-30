from django_seed import Seed
from .models import Category, Product

def runProduct():
    seeder = Seed.seeder()
    
    categories = [
    {'value': 'Sports Car'},
    {'value': 'Electric Car'},
    {'value': 'Luxury Car'},
    {'value': 'SUV'},
    {'value': 'Trucks'},
]


    for item in categories:
        seeder.add_entity(Category, 1, item)
    
    print(seeder.execute())
    
    
    #----------------------------------------------------------------
    
    products = [
        
        {
            'img1': 'https://prod.pictures.autoscout24.net/listing-images/70de98be-f3b8-4eff-afd9-dac2e918e650_fa471dc8-e4a9-4dd7-b57b-22e1659e2d03.jpg/720x540.webp',
            'img2': 'https://prod.pictures.autoscout24.net/listing-images/70de98be-f3b8-4eff-afd9-dac2e918e650_a5e511e9-eef2-4ce5-8fdf-6ddb333e6f3e.jpg/720x540.webp',
            'img3': 'https://prod.pictures.autoscout24.net/listing-images/70de98be-f3b8-4eff-afd9-dac2e918e650_9aacac80-267f-457f-8357-323d36391657.jpg/720x540.webp',
            'description': 'The Porsche 911 GT3 is an iconic sports car known for its thrilling performance and precision handling. With a powerful engine and aerodynamic design, the 911 GT3 delivers an exhilarating driving experience on both the track and the road. Its luxurious interior and advanced technology make it a dream car for enthusiasts and thrill-seekers alike.',
            'name': 'Porsche 911 GT3',
            'category': Category.objects.all()[0],
            'price': 150000,
            'promo': 0,
            'stock': {
                '0-10,000 km': 3,
                '10,000-30,000 km': 5,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 2,
            },
        },
        {
            'img1': 'https://prod.pictures.autoscout24.net/listing-images/1d07dca1-afd3-4ae6-b828-a91557e3928b_c3437e6f-0a1f-4d15-a522-b2580ff01b16.jpg/720x540.webp',
            'img2': 'https://prod.pictures.autoscout24.net/listing-images/1d07dca1-afd3-4ae6-b828-a91557e3928b_0a11e671-123f-415f-a9b1-7c434e329552.jpg/720x540.webp',
            'img3': 'https://prod.pictures.autoscout24.net/listing-images/1d07dca1-afd3-4ae6-b828-a91557e3928b_b284fc38-88a1-4a5e-a4dd-3a9d0bca7a99.jpg/720x540.webp',
            'description': 'The Porsche 911 GT2 is an iconic sports car known for its thrilling performance and precision handling. With a powerful engine and aerodynamic design, the 911 GT3 delivers an exhilarating driving experience on both the track and the road. Its luxurious interior and advanced technology make it a dream car for enthusiasts and thrill-seekers alike.',
            'name': 'Porsche 911 GT2',
            'category': Category.objects.all()[0],
            'price': 150000,
            'promo': 0,
            'stock': {
                '0-10,000 km': 3,
                '10,000-30,000 km': 5,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 2,
            },
        },
        {
            'img1': 'https://prod.pictures.autoscout24.net/listing-images/7f0bb2c2-49a0-4dcc-92d0-14353fdffd94_ed5d4ed5-4d21-47cf-b62a-22f7d484d899.jpg/720x540.webp',
            'img2': 'https://prod.pictures.autoscout24.net/listing-images/7f0bb2c2-49a0-4dcc-92d0-14353fdffd94_6e376174-8b5e-4fb1-ab6d-05ec2e0deacf.jpg/720x540.webp',
            'img3': 'https://prod.pictures.autoscout24.net/listing-images/7f0bb2c2-49a0-4dcc-92d0-14353fdffd94_5e78e11f-daeb-40c0-aa48-9cb6d9837c74.jpg/720x540.webp',
            'description': 'The Mercedes-Benz S-Class Cabriolet is the epitome of luxury and style. With its elegant design and refined features, this convertible offers a comfortable and sophisticated driving experience. The S-Class Cabriolets advanced technology and premium materials make every journey a memorable one, whether youre cruising through the city or enjoying a scenic road trip.',
            'name': 'Mercedes-Benz',
            'category': Category.objects.all()[0],
            'price': 100000,
            'promo': 0,
            'stock': {
                '0-10,000 km': 3,
                '10,000-30,000 km': 5,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 2,
            },
        },
        {
            'img1': 'https://prod.pictures.autoscout24.net/listing-images/b89866bd-17ae-4edd-9a6c-5b3c0fb1b8ca_bdae0948-3fb2-45a1-8fc4-cbe8aacb42c6.jpg/720x540.webp',
            'img2': 'https://prod.pictures.autoscout24.net/listing-images/b89866bd-17ae-4edd-9a6c-5b3c0fb1b8ca_c879a251-f21a-4200-afde-6194324b182b.jpg/720x540.webp',
            'img3': 'https://prod.pictures.autoscout24.net/listing-images/b89866bd-17ae-4edd-9a6c-5b3c0fb1b8ca_16c92083-c864-4547-a48a-1a44b3b06a75.jpg/720x540.webp',
            'description': 'The Ford Explorer is a versatile SUV that offers spacious seating and impressive performance. With its rugged design and powerful engine options, the Explorer is ready for all types of adventures. Whether youre exploring off-road trails or navigating city streets, the Ford Explorer provides a comfortable and capable driving experience for families and outdoor enthusiasts.',
            'name': 'Ford Explorer',
            'category': Category.objects.all()[3],
            'price': 90000,
            'stock': {
                '0-10,000 km': 4,
                '10,000-30,000 km': 3,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 6,
            },
        },
        {
            'img1': 'https://prod.pictures.autoscout24.net/listing-images/d157c51b-2dc5-4e1d-8048-57e77a82fdd6_366f7b42-b395-4056-baa9-f4e871b833d3.jpg/720x540.webp',
            'img2': 'https://prod.pictures.autoscout24.net/listing-images/d157c51b-2dc5-4e1d-8048-57e77a82fdd6_7e78e853-53ac-4854-9021-db2fdf4c4b0f.jpg/720x540.webp',
            'img3': 'https://prod.pictures.autoscout24.net/listing-images/d157c51b-2dc5-4e1d-8048-57e77a82fdd6_97106354-1c3d-4f47-830c-aec80a229242.jpg/720x540.webp',
            'description': 'The Ford Mustang is a versatile Sportcar that offers spacious seating and impressive performance. With its rugged design and powerful engine options, the Explorer is ready for all types of adventures. Whether youre exploring off-road trails or navigating city streets, the Ford Explorer provides a comfortable and capable driving experience for families and outdoor enthusiasts.',
            'name': 'Ford Mustang',
            'category': Category.objects.all()[2],
            'price': 120000,
            'stock': {
                '0-10,000 km': 4,
                '10,000-30,000 km': 3,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 6,
            },
        },
        {
            'img1': 'https://prod.pictures.autoscout24.net/listing-images/4d2cb727-0b50-4f99-826f-1299b68f7719_02486ac9-524b-4297-a992-0c32e8cc8420.jpg/720x540.webp',
            'img2': 'https://prod.pictures.autoscout24.net/listing-images/4d2cb727-0b50-4f99-826f-1299b68f7719_ebc15e7f-d866-4252-8746-734a1e166fbe.jpg/720x540.webp',
            'img3': 'https://prod.pictures.autoscout24.net/listing-images/4d2cb727-0b50-4f99-826f-1299b68f7719_9375ba47-a354-40e7-99a5-f843868036fa.jpg/720x540.webp',
            'description': 'The Nissan Leaf is a popular all-electric hatchback known for its practicality and eco-friendliness. With a spacious interior and impressive range, the Leaf is perfect for daily commutes and city driving. Its modern design and advanced features make it an appealing choice for environmentally-conscious drivers seeking an affordable and efficient electric car.',
            'name': 'Nissan Leaf',
            'category': Category.objects.all()[1],
            'price': 36000,
            'stock': {
                '0-10,000 km': 4,
                '10,000-30,000 km': 3,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 6,
            },
        },
        {
            'img1': 'https://media.gettyimages.com/photos/monster-truck-performs-at-the-capitol-centre-in-landover-maryland-08-picture-id51674057',
            'img2': 'https://media.gettyimages.com/photos/monster-truck-performs-at-the-capitol-centre-in-landover-maryland-08-picture-id51674057',
            'img3': 'https://media.gettyimages.com/photos/monster-truck-performs-at-the-capitol-centre-in-landover-maryland-08-picture-id51674057',
            'description': 'The MonsterTruck is a popular truck known for its practicality and eco-friendliness. With a spacious interior and impressive range, the Leaf is perfect for daily commutes and city driving. Its modern design and advanced features make it an appealing choice for environmentally-conscious drivers seeking an affordable and efficient electric car.',
            'name': 'Monster Truck',
            'category': Category.objects.all()[4],
            'price': 36000,
            'stock': {
                '0-10,000 km': 4,
                '10,000-30,000 km': 3,
                '30,000-50,000 km': 2,
                '50,000-70,000 km': 1,
                '70,000+ km': 6,
            },
        },


    ]
    
    for item in products:
        seeder.add_entity(Product, 1, item)
    print(seeder.execute())
    
        
