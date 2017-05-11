from handlers.base_handler import BaseHandler

db = {
    1:{'id':1, 'name':'Fido', 'image_url':'https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg'},
    2:{'id':2, 'name': 'Cesar', 'image_url':'http://3.bp.blogspot.com/-NAJ179pS4VU/Up3IKdKSnVI/AAAAAAAAAvg/mGshsQ078Gk/s1600/bom-dia.jpg'}
}

class ShowDogHandler(BaseHandler):
    def get(self, id=None):
        dog = db.get(int(id))
        if dog:
            self.render("dogs/show.html", dog=dog)
        else:
            self.write("No dog found for id {}".format(id))

class CreateDogHandler(BaseHandler):
    def get(self):
        self.render("dogs/create.html", dog=None)

    def post(self):
        name = self.request.params['name']
        url = self.request.params['image_url']
        self.write("Creating dog {}".format(name))

class EditDogHandler(BaseHandler):
    def get(self, id=None):
        dog = db.get(int(id))
        if dog:
            self.render("dogs/edit.html", dog=dog)
        else:
            self.write("No dog found for id {}".format(id))

    def post(self, id=None):
        name = self.request.params['name']
        url = self.request.params['image_url']
        self.write("Editing dog {}".format(name))
