#import imagecutcontroller as ICC
import DBcontroller as DBC






#def request_images(location, email):
#    order = ICC.runimagecutcontroller(location, email)


def get_footprint_from_db(imageid):
    image = DBC.get_footprint_from_db(imageid)
    return image

def get_camera_width_height(cameraid, coneid):
    width, height = DBC.get_camera_width_height(cameraid, coneid)
    return width, height

def create_order(order):
    DBC.create_order(order)

def update_order(order):
    DBC.update_order(order)




