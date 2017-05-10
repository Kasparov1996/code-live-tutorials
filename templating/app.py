from router import Router
from handlers.dog_handlers import ShowDogHandler, CreateDogHandler, EditDogHandler
from handlers.cat_handlers import CatHandler

app = Router()

app.handle(r'^/dog/(?P<id>[\d]+)$', ShowDogHandler)
app.handle("/dog/create", CreateDogHandler, methods=['GET', 'POST'])
app.handle("/dog/(?P<id>[\d]+)/edit", EditDogHandler, methods=['GET', 'POST'])
app.handle('/cat', CatHandler)


