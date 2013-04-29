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
		<table border = "1">
		<tr>
		<th>Children's</th>
		<th>Women's</th>
		<th>Men's</th>
		</tr>
		<td>
		<input type="radio" name="size" value=0 /> X-Small <br />
                <input type="radio" name="size" value=1 /> Small <br />
                <input type="radio" name="size" value=2 /> Medium <br />
                <input type="radio" name="size" value=3 /> Large <br />
                <input type="radio" name="size" value=4 /> X-Large <br />
		</td>
		<td>
		<input type="radio" name="size" value=5 /> X-Small <br />
                <input type="radio" name="size" value=6 /> Small <br />
                <input type="radio" name="size" value=7 /> Medium <br />
                <input type="radio" name="size" value=8 /> Large <br />
                <input type="radio" name="size" value=9 /> X-Large <br />
		</td>
		<td>
		<input type="radio" name="size" value=10 /> X-Small <br />
                <input type="radio" name="size" value=11 /> Small <br />
                <input type="radio" name="size" value=12 /> Medium <br />
                <input type="radio" name="size" value=13 /> Large <br />
                <input type="radio" name="size" value=14 /> X-Large <br />
		</td>
		</table>
		<br />
                Shape: <br />
                <input type="radio" name="shape" value="0" /> classic <br />
                <br />
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
        sleeve = [16.5, 17, 17, 17.5, 17.5] #sleeve length to underarm (l + m)
        arm = [9.75, 10.25, 11, 12, 13.5]
        armhole = [6.5, 7, 7.5, 8, 8.5] #depth
        waist = [23.5, 26, 29, 31, 37]
        hips = [33.5, 35.5, 39, 43, 47]
        wrist = [7, 7.5, 8, 8.5, 9]
        form = cgi.FieldStorage()
        gauge = float(form.getvalue('gauge'))
        gHeight = int(form.getvalue('height'))
        gWidth = int(form.getvalue('width'))
        # set size
        #strSize = form.getvalue('size')
        #if strSize == 'xs':
        #    size = 0
        #elif strSize == 's':
        #    size = 1
        #elif strSize == 'm':
        #    size = 2
        #elif strSize == 'l':
        #    size = 3
        #else:
        #    size = 4
	size = int(form.getvalue('size'))
        # shape (set picture)
        shape = int(form.getvalue('shape'))
        if shape == 0:
            picture = 'classic.png'
        data_uri = open(picture, 'rb').read().encode('base64').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        self.response.out.write(img_tag)
        self.response.out.write('<html><body><pre>')
        
        a = armhole[size]+length2[size]
        self.response.out.write('\nA:')
	self.response.out.write(a)
	self.response.out.write(' inches (')
	self.response.out.write(int(a * gHeight))
	self.response.out.write(' stitches)')
	
	b = hips[size]/2
	self.response.out.write('\nB:')
	self.response.out.write(b)
	self.response.out.write(' inches (')
	self.response.out.write(int(b * gWidth))
	self.response.out.write(' stitches)')
	
	c = length2[size]
	self.response.out.write('\nC:')
	self.response.out.write(c)
	self.response.out.write(' inches (')
	self.response.out.write(int(c * gHeight))
	self.response.out.write(' stitches)')
	
	d = armhole[size]/2
	self.response.out.write('\nD:')
	self.response.out.write(d)
	self.response.out.write(' inches (')
	self.response.out.write(int(d * gHeight))
	self.response.out.write(' stitches)')
	
	e = armhole[size]/4
	self.response.out.write('\nE:')
	self.response.out.write(e)
	self.response.out.write(' inches (')
	self.response.out.write(int(e * gHeight))
	self.response.out.write(' stitches)')
	
	f = armhole[size]/4
	self.response.out.write('\nF:')
	self.response.out.write(f)
	self.response.out.write(' inches (')
	self.response.out.write(int(f * gHeight))
	self.response.out.write(' stitches)')
	
	g = shoulder[size]
	self.response.out.write('\nG:')
	self.response.out.write(g)
	self.response.out.write(' inches (')
	self.response.out.write(int(g * gWidth))
	self.response.out.write(' stitches)')
	
	h = round(shoulder[size]*.54, 0)
	self.response.out.write('\nH:')
	self.response.out.write(h)
	self.response.out.write(' inches (')
	self.response.out.write(int(h * gWidth))
	self.response.out.write(' stitches)')
	
	i = (shoulder[size] - h) / 2
	self.response.out.write('\nI:')
	self.response.out.write(i)
	self.response.out.write(' inches (')
	self.response.out.write(int(i * gWidth))
	self.response.out.write(' stitches)')
	
	centerToSleeve = (h / 2) + i
	j = neckCuff[size] - centerToSleeve
	self.response.out.write('\nJ:')
	self.response.out.write(j)
	self.response.out.write(' inches (')
	self.response.out.write(int(j * gHeight))
	self.response.out.write(' stitches)')
	
	k = wrist[size]
	self.response.out.write('\nK:')
	self.response.out.write(k)
	self.response.out.write(' inches (')
	self.response.out.write(int(k * gWidth))
	self.response.out.write(' stitches)')
	
	l = 2
	self.response.out.write('\nL:')
	self.response.out.write(l)
	self.response.out.write(' inches (')
	self.response.out.write(int(l * gHeight))
	self.response.out.write(' stitches)')
	
	m = sleeve[size] - l
	self.response.out.write('\nM:')
	self.response.out.write(m)
	self.response.out.write(' inches (')
	self.response.out.write(int(m * gHeight))
	self.response.out.write(' stitches)')
	
	n = j - sleeve[size]
	self.response.out.write('\nN:')
	self.response.out.write(n)
	self.response.out.write(' inches (')
	self.response.out.write(int(n * gHeight))
	self.response.out.write(' stitches)')
	
	o = arm[size]
	self.response.out.write('\nO:')
	self.response.out.write(o)
	self.response.out.write(' inches (')
	self.response.out.write(int(o * gWidth))
	self.response.out.write(' stitches)')
	
	sleeveArea = (k*l + m*(o+k)/2 + n*(o+i)/2)*2
	bodyArea = (b*c*2 + g*d + (e+f)*i*2 + g*(d+e) + i*f*2 + .2*g*d)
	totalArea = float(sleeveArea + bodyArea)
	yarn = totalArea * gauge
	self.response.out.write('\n\nAmount of yarn needed: ')
	self.response.out.write(yarn)
	self.response.out.write(' yards')
        self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/print', Sweater)],
                              debug=True)
