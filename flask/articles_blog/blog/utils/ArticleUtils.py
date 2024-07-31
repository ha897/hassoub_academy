from blog import cfg
import os,secrets

def save_image(image_file):
    # للامان نقوم بتغيير اسم الصورة لاعداد عشوائية
    # تقوم بعض الاسماء بمشاكل عند حفضها بالسرفر عشان كذا نغيره
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(image_file.filename)
    image_new_name = random_hex + file_ext
    # امتداد الصورة الجديدة يكون بملف الصور
    image_path = os.path.join(cfg.IMAGES_DIR, image_new_name)
    #حفض بالمسار المحدد
    image_file.save(image_path)
    
    return image_new_name