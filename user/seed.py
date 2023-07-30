from django_seed import Seed
from user.models import Role, User
from django.contrib.auth.hashers import make_password

def runConnexion():
    seeder = Seed.seeder()

    # Ajouter les rôles
    roles = [
        {'value': Role.ADMIN},
        {'value': Role.WEB},
        {'value': Role.MEMBER},
    ]
    
    for item in roles:
        role, created = Role.objects.get_or_create(value=item['value'])
        if created:
            print(f"Role {role} created.")
    
    # Ajouter les utilisateurs
    users = [
        {'username': 'admin2', 'email': 'admin@gmail.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.ADMIN), 'img_url' : 'https://sm.ign.com/ign_fr/cover/a/avatar-gen/avatar-generations_bssq.jpg'},
        {'username': 'web', 'email': 'web@gmail.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.WEB), 'img_url' : 'https://static.vecteezy.com/ti/vecteur-libre/p3/3731316-web-icon-vector-line-on-white-background-image-for-web-presentation-logo-icon-symbol-gratuit-vectoriel.jpg'},
        {'username': 'member', 'email': 'member@gmail.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.MEMBER), 'img_url' : 'https://accws.org/wp-content/uploads/2014/04/member-stamp.jpg'},
    ]
    
    for item in users:
        seeder.add_entity(User, 1, item)
    
    # Execute the seeder after adding all entities
    inserted_pks = seeder.execute()
    print(inserted_pks)

runConnexion()
