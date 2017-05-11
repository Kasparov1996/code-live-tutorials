from handlers.base_handler import BaseHandler

class CatHandler(BaseHandler):
    def get(self):
        if self.request.cookies.get('remember'):
            self.write("Cat is remembered. Click to forget <a href='/cats/forget'>forget</a>!")
        else:
            self.render("cats/form.html")

    def post(self):
        self.response.set_cookie('remember', "1")
        self.redirect("/cats")

class ForgetCatHandler(BaseHandler):
    def get(self):
        self.response.delete_cookie("remember")
        self.redirect("/cats")
