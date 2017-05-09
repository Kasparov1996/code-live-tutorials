from router import Router
from handlers import DogHandler, CatHandler

app = Router()

app.handle(r'^/dog/(?P<id>[\d]+)$', DogHandler)
app.handle('/cat', CatHandler)


