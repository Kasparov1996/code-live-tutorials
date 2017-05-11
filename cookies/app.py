from router import Router
from handlers.dog_handlers import ShowDogHandler, CreateDogHandler, EditDogHandler
from handlers.cat_handlers import CatHandler, ForgetCatHandler

app = Router()

app.handle(r'^/dogs/(?P<id>[\d]+)$', ShowDogHandler)
app.handle("/dogs/create", CreateDogHandler, methods=['GET', 'POST'])
app.handle("/dogs/(?P<id>[\d]+)/edit", EditDogHandler, methods=['GET', 'POST'])
app.handle('/cats', CatHandler, methods=['GET', 'POST'])
app.handle('/cats/forget', ForgetCatHandler)


