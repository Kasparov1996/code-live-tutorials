from handlers.base_handler import BaseHandler

db = {
    1:{'id':1, 'name':'Fido', 'image_url':'https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg'},
    2:{'id':2, 'name': 'cesar', 'image_url':'http://3.bp.blogspot.com/-NAJ179pS4VU/Up3IKdKSnVI/AAAAAAAAAvg/mGshsQ078Gk/s1600/bom-dia.jpg'}
}

class ShowDogHandler(BaseHandler):
    def get(self, id=None):
        dog = db.get(int(id))
        if dog:
            self.response.write(self.render("show_dog.html", **dog))
        else:
            self.response.write("No dog found for id {}".format(id))

class CreateDogHandler(BaseHandler):
    def get(self):
        self.response.write(self.render("create_dog.html", name="", image_url=""))

    def post(self):
        name = self.request.params['name']
        url = self.request.params['image_url']
        self.response.write("Creating dog {}".format(name))

class EditDogHandler(BaseHandler):
    def get(self, id=None):
        dog = db.get(int(id))
        if dog:
            self.response.write(self.render("create_dog.html", **dog))
        else:
            self.response.write("No dog found for id {}".format(id))

    def post(self):
        name = self.request.params['name']
        url = self.request.params['image_url']
        self.response.write("Editing dog {}".format(name))
