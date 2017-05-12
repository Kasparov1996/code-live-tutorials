from handlers.base_handler import BaseHandler

class CatHandler(BaseHandler):
    def get(self):
        if self.request.cookies.get('remember'):
            self.render("cats/index.html")
        else:
            self.render("cats/form.html")

    def post(self):
        if self.request.params.get('remember') == "on":
            self.response.set_cookie('remember', "1")
        self.redirect("/cats")

class ForgetCatHandler(BaseHandler):
    def get(self):
        self.response.delete_cookie("remember")
        self.redirect("/cats")
