import carla
from PIL import Image

def stream_patch(world):

    # define adversarial image path
    adv_image_path_base = 'leaderboard/leaderboard/patches/'
    adv_image_name = 'color_patch.png'
    adv_image_path = adv_image_path_base + adv_image_name

    # define road regions
    corner = [31, 27, 23, 19, 15, 11]
    before_corner = [3, 7]
    after_corner = [35, 39]
    patch0 = [85, 93]
    patch1 = [109, 117]
    patch2 = [262, 184]
    patch3 = [263, 185]
    patch4 = [264, 186]
    patch5 = [142, 220]
    patch6 = [141, 219]
    patch7 = [140, 218]

    # set which region to apply adversarial texture
    numbers = corner

    # load adversarial texture image and create texture object
    image = Image.open(adv_image_path)
    width, height = image.size
    adv_texture = carla.TextureColor(width, height)
    for x in range(0,width):
        for y in range(0,height):
            color = image.getpixel((x,y))
            r = int(color[0])
            g = int(color[1])
            b = int(color[2])
            a = 255
            adv_texture.set(x, y, carla.Color(r,g,b,a))

    # stream adversarial texture to specific roads
    for number in numbers:
        world.apply_color_texture_to_object('Road_Road_Town02_' + str(number), carla.MaterialParameter.Diffuse, adv_texture)