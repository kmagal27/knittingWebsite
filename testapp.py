import cgi, cgitb
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
              <form action="/print" method="get">
                Gauge Square:
                Stitches per square inch (height): <input type="integer" name="height"/> <br />
                Stitches per square inch (width): <input type="integer" name="width"/> <br />
                Length of yarn (yards): <input type="integer" name="gauge"/> <br />
                <br />
                Size: <br />
                <input type="radio" name="size" value="xs" /> X-Small <br />
                <input type="radio" name="size" value="s" /> Small <br />
                <input type="radio" name="size" value="m" /> Medium <br />
                <input type="radio" name="size" value="l" /> Large <br />
                <input type="radio" name="size" value="xl" /> X-Large <br />
                <input type="submit" value="Calculate">
              </form>
            </body>
          </html>""")

class Sweater(webapp2.RequestHandler):
    def get(self):
        bust = [29, 33, 37, 41, 45]
        neckCuff = [27.5, 28.5, 29.5, 30.5, 31.5] #center back to neck cuff
        length2 = [16.5, 17, 17.25, 17.5, 17.75] #back waist length
        shoulder = [14.5, 15, 16.5, 17.5, 17.5] #cross back
        sleeve = [16.5, 17, 17, 17.5, 17.5] #sleeve length to underarm
        arm = [9.75, 10.25, 11, 12, 13.5]
        armhole = [6.5, 7, 7.5, 8, 8.5] #depth
        waist = [23.5, 26, 29, 31, 37]
        hips = [33.5, 35.5, 39, 43, 47]
        form = cgi.FieldStorage()
        strSize = form.getvalue('size')
        if strSize == 'xs':
            size = 0
        elif strSize == 's':
            size = 1
        elif strSize == 'm':
            size = 2
        elif strSize == 'l':
            size = 3
        else:
            size = 4
        data_uri = open('standard.png', 'rb').read().encode('base64').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        self.response.out.write(img_tag)
        self.response.out.write('<html><body><pre>')
        self.response.out.write('\na:')
	self.response.out.write(armhole[size]+length2[size])
	self.response.out.write('\nb:')
	self.response.out.write(shoulder[size])
        self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/print', Sweater)],
                              debug=True)
