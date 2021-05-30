import imagecutcontroller as ICC



def get_requested_images(location, email):
    order = ICC.run_imagecutcontroller(location, email)
