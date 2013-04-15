import cgi
import webapp2

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <head>
              <title> Knitting Page </title>
            </head>
            <body>
              <form action="/sign" method="post">
                <div> Length: <input type="integer" name="length"/></div>
                <div><input type="submit" value="Add 2"></div>
              </form>
            </body>
          </html>""")


class Guestbook(webapp2.RequestHandler):
    def post(self):
        leng = cgi.FieldStorage()
        self.response.out.write(leng["length"])
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('length')))
        self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/sign', Guestbook)],
                              debug=True)
