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
        {'username': 'admin2', 'email': 'admin@gmail.com', 'password': make_password('3914'), 'role': Role.objects.get(value=Role.ADMIN), 'img_url' : 'https://www.bing.com/images/search?view=detailV2&ccid=4AqXavpE&id=6E7202775791631DD5F2ACEAD9451313406C2A26&thid=OIP.4AqXavpE3Z_lv7K8cuVRpAAAAA&mediaurl=https%3a%2f%2fimage.noelshack.com%2ffichiers%2f2017%2f15%2f1492300687-misterv.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.e00a976afa44dd9fe5bfb2bc72e551a4%3frik%3dJipsQBMTRdnqrA%26pid%3dImgRaw%26r%3d0&exph=441&expw=474&q=mister+kadrix&simid=608036768279513292&FORM=IRPRST&ck=82E302DB0E0EF2AB677DA417CCD1DBDC&selectedIndex=4&ajaxhist=0&ajaxserp=0'},
        {'username': 'web', 'email': 'web@gmail.com', 'password': make_password('3914'), 'role': Role.objects.get(value=Role.WEB), 'img_url' : 'https://www.bing.com/images/search?view=detailV2&ccid=AVHQj4u%2b&id=39305903B2E15B712268BE2AAE7BAE16E521F415&thid=OIP.AVHQj4u-PjUdyiBjSm6LpgHaJ4&mediaurl=https%3a%2f%2fpbs.twimg.com%2fmedia%2fB_kuMEPWwAEQvjL.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.0151d08f8bbe3e351dca20634a6e8ba6%3frik%3dFfQh5Raue64qvg%26pid%3dImgRaw%26r%3d0&exph=1024&expw=768&q=mister+v&simid=608027778937390528&FORM=IRPRST&ck=B960EEE21A6543D78FA7870FF94ECE87&selectedIndex=118&ajaxhist=0&ajaxserp=0'},
        {'username': 'member', 'email': 'member@gmail.com', 'password': make_password('3914'), 'role': Role.objects.get(value=Role.MEMBER), 'img_url' : 'https://www.bing.com/images/search?view=detailV2&ccid=SOkBs1q8&id=CF617169AE2E6F1E4E25DBD32EB2D0CB79B80FD8&thid=OIP.SOkBs1q8EolMrtT90MrVwwHaI_&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.48e901b35abc12894caed4fdd0cad5c3%3frik%3d2A%252b4ecvQsi7T2w%26riu%3dhttp%253a%252f%252fimages.memes.com%252fmeme%252f1020853%26ehk%3d34IHEwwHgEF1U0%252bhyFk6iVPLuqtmQZom2NjrcRkD2es%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=775&expw=638&q=meme&simid=608008752212368354&FORM=IRPRST&ck=D14B0176EE4C0251DD2C2D31ADF4900F&selectedIndex=40&ajaxhist=0&ajaxserp=0'},
    ]
    
    for item in users:
        seeder.add_entity(User, 1, item)
    
    # Execute the seeder after adding all entities
    inserted_pks = seeder.execute()
    print(inserted_pks)

runConnexion()
