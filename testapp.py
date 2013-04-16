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
                <div> Stitches per square inch (height): <input type="integer" name="height"/></div>
                <div> Stitches per square inch (width): <input type="integer" name="width"/></div>
                <div> Hips: <input type="integer" name="hips"/></div>
                <div> Waist: <input type="integer" name="waist"/></div>
                <div> Bust: <input type="integer" name="bust"/></div>
                <div> Shoulder Width: <input type="integer" name="shoulder"/></div>
                <div> Length: <input type="integer" name="length"/></div>
                <div><input type="submit" value="Calculate"></div>
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
