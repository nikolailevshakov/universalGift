from PIL import Image, ImageFont, ImageDraw
import os, shutil, random


def generate_certificate(template_file, user_file, host, name):
    i = Image.open(f"static/{template_file}")
    user = Image.open(f"images/{user_file}")
    Im = ImageDraw.Draw(i)

    mf_who = ImageFont.truetype('static/Unbounded-Regular.ttf', 22)
    mf_header = ImageFont.truetype('static/Unbounded-Regular.ttf', 16)
    mf_name = ImageFont.truetype('static/Unbounded-Regular.ttf', 54)

    Im.text((100, 1010), "Владелец:", fill=(129,133,137), font=mf_header)
    Im.text((98, 1030), f"{host}", fill=(255,255,255), font=mf_who)
    Im.text((490, 1010), "Координаты:", fill=(129,133,137), font=mf_header)
    Im.text((400, 1030), f"{random.randint(1, 99)}.{random.randint(100000, 999999)}°, {random.randint(1, 99)}.{random.randint(100000, 999999)}°", fill=(255,255,255), font=mf_who)
    Im.text((140, 920), f"{name}", fill=(223,255,32), font=mf_name)

    mask_im = Image.new("L", user.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((100, 10, 700, 610), fill=255)
    mask_im.save('images/mask_circle.jpg', quality=95)

    i.paste(user, (-15, 190), mask_im)
    i.save('images/cert.jpg', quality=95)


def clear_folder():
    folder = 'images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
