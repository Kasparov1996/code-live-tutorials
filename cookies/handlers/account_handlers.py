from handlers.base_handler import BaseHandler
import hmac
import config

accounts = {'vince':{'username':'vince', 'password':'1234'}}



class AccountHandler(BaseHandler):
    def make_secure_value(self, value):
        return "{}|{}".format(value, hmac.new(config.SECRET_KEY.encode(),
                                              value.encode()).hexdigest())

    def check_secure_value(self, secure_value):
        val = secure_value.split('|')
        if secure_value == self.make_secure_value(val):
            return val

    def set_secure_cookie(self, name, val):
        cookie_val = self.make_secure_value(val)
        self.response.set_cookie(name, cookie_val)

    def get_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        if cookie_val and self.check_secure_value(cookie_val):
            return cookie_val
        return None

    def login(self, user):
        self.set_secure_cookie('username', str(user['username']))

    def logout(self, user):
        self.response.delete_cookie('username')



class SignupHandler(AccountHandler):
    def get(self):
        self.render("accounts/signup.html")

    def post(self):
        username = self.request.params.get('username')
        password = self.request.params.get('password')
        accounts[username] = {'username': username, 'password':password}
        print(accounts)
        self.redirect('/cats')


class LoginHandler(AccountHandler):
    def get(self):
        self.render("accounts/login.html", errors="")

    def post(self):
        errors = []
        username = self.request.params.get('username')
        password = self.request.params.get('password')
        user = accounts.get(username, None)
        if user is None:
            errors.append('username does not exist')
        if user and password != user['password']:
            errors.append("password is not correct")
        if user and password == user['password']:
            self.login(user)
            return self.redirect('/cats')
        self.render("accounts/login.html", errors=errors)


class LogoutHandler(AccountHandler):
    def get(self):
        self.write("<h1>Logout</h1>")