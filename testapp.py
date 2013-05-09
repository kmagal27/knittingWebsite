import cgi, cgitb
import webapp2

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        title_pic = 'title.png'
        data_uri = open(title_pic, 'rb').read().encode('base64').replace('\n', '')
        title_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        self.response.out.write(title_tag)
        self.response.out.write("""
        <style>
	   body{ font-family: verdana;
		font-size: 18px;
		margin-left: 50px;}
	</style>
	 <html>
            <head>
              <title> Sweater Generator </title>
            </head>
            <body>
              <form action="/print" method="get">
                Gauge Square: <br />
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
		<input type="radio" name="size" value=0 /> 2 <br />
                <input type="radio" name="size" value=1 /> 4 <br />
                <input type="radio" name="size" value=2 /> 6 <br />
                <input type="radio" name="size" value=3 /> 8 <br />
                <input type="radio" name="size" value=4 /> 10 <br />
                <input type="radio" name="size" value=5 /> 12 <br />
                <input type="radio" name="size" value=6 /> 14 <br />
                <input type="radio" name="size" value=7 /> 16 <br />
		</td>
		<td>
		<input type="radio" name="size" value=8 /> X-Small <br />
                <input type="radio" name="size" value=9 /> Small <br />
                <input type="radio" name="size" value=10 /> Medium <br />
                <input type="radio" name="size" value=11 /> Large <br />
                <input type="radio" name="size" value=12 /> X-Large <br />
		</td>
		<td>
                <input type="radio" name="size" value=13 /> Small <br />
                <input type="radio" name="size" value=14 /> Medium <br />
                <input type="radio" name="size" value=15 /> Large <br />
                <input type="radio" name="size" value=16 /> X-Large <br />
                <input type="radio" name="size" value=17 /> XX-Large <br />
		</td>
		</table>
		<br />
                Shape: <br />
                <input type="radio" name="shape" value="0" /> Classic <br />
                <input type="radio" name="shape" value="1" /> Double Taper <br />
                <input type="radio" name="shape" value="2" /> Single Taper <br />
                <br />
                <input type="submit" value="Calculate">
              </form>
            </body>
          </html>""")

class Sweater(webapp2.RequestHandler):
    def get(self):
        title_pic = 'title.png'
        data_uri = open(title_pic, 'rb').read().encode('base64').replace('\n', '')
        title_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        self.response.out.write(title_tag)
        self.response.out.write("<br />")
        bust = [21, 23, 25, 26.5, 28, 30, 31.5, 32.5, 29, 33, 37, 41, 45, 35, 39, 43, 47, 51]
        neckCuff = [18, 19.5, 20.5, 22, 24, 26, 27, 28, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5] #center back to neck cuff
        length2 = [8.5, 9.5, 10.5, 12.5, 14, 15, 15.5, 16, 16.5, 17, 17.25, 17.5, 17.75, 25.5, 26.75, 27.5, 27.75, 28.5] #back waist length
        shoulder = [9.25, 9.75, 10.25, 10.75, 11.25, 12, 12.25, 13, 14.5, 15, 16.5, 17.5, 17.5, 16, 17, 18, 18.5, 19] #cross back
        sleeve = [8.25, 10.5, 11.5, 12.5, 13.5, 15, 16, 16.5, 16.5, 17, 17, 17.5, 17.5, 18, 18.5, 19.5, 20, 20.5] #sleeve length to underarm (l + m)
        arm = [7, 7.5, 8, 8.5, 8.75, 9, 9.25, 9.5, 9.75, 10.25, 11, 12, 13.5, 12, 13, 15, 16, 17]
        armhole = [4.25, 4.75, 5, 5.5, 6, 6.5, 7, 7.5, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11] #depth
        waist = [21, 21.5, 22.5, 23.5, 24.5, 25, 26.5, 27.5, 23.5, 26, 29, 31, 37, 29, 33, 37, 43, 47]
        hips = [22, 23.5, 25, 28, 29.5, 31.5, 33, 35.5, 33.5, 35.5, 39, 43, 47, 36, 40, 44, 48, 52]
        wrist = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 7, 7.5, 8, 8.5, 9, 8, 8.5, 9, 9.5, 10]
        form = cgi.FieldStorage()
        gauge = float(form.getvalue('gauge'))
        gHeight = int(form.getvalue('height'))
        gWidth = int(form.getvalue('width'))
	size = int(form.getvalue('size'))
        # shape (set picture)
        shape = int(form.getvalue('shape'))
        if shape == 0:
            picture = 'classic.png'
        elif shape == 1:
            picture = 'double_taper.png'
        elif shape == 2:
            picture = 'single_taper.png'
        data_uri = open(picture, 'rb').read().encode('base64').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        self.response.out.write(img_tag)
	self.response.out.write("""
	<style>
	   body{ font-family: verdana;
		font-size: 16px;
		margin-left: 50px;}
	</style>""")
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

	if shape == 0:
            c = length2[size]
        elif shape == 1:
            c = round((length2[size] - 2)/2, 1)
        elif shape == 2:
            if size < 8:
                c = length2[size] - 1
            else:
                c = length2[size] - 2
	self.response.out.write('\nC:')
	self.response.out.write(c)
	self.response.out.write(' inches (')
	self.response.out.write(int(c * gHeight))
	self.response.out.write(' stitches)')

	if shape == 0 or shape == 2:
            d = armhole[size]/2
        elif shape == 1:
            d = c
	self.response.out.write('\nD:')
	self.response.out.write(d)
	self.response.out.write(' inches (')
	self.response.out.write(int(d * gHeight))
	self.response.out.write(' stitches)')

	if shape == 0 or shape == 2:
            e = armhole[size]/4
        elif shape == 1:
            e = round(armhole[size] * 2 / 3, 1)
	self.response.out.write('\nE:')
	self.response.out.write(e)
	self.response.out.write(' inches (')
	self.response.out.write(int(e * gHeight))
	self.response.out.write(' stitches)')

	if shape == 0 or shape == 2:
            f = armhole[size]/4
        elif shape == 1:
            f = round(armhole[size]/3, 1)
	self.response.out.write('\nF:')
	self.response.out.write(f)
	self.response.out.write(' inches (')
	self.response.out.write(int(f * gHeight))
	self.response.out.write(' stitches)')
	
	g = shoulder[size]
	if shape != 2:
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

	if shape == 0 or shape == 2:
            k = wrist[size]
        elif shape == 1:
            k = round(wrist[size]*1.2, 1)
	self.response.out.write('\nK:')
	self.response.out.write(k)
	self.response.out.write(' inches (')
	self.response.out.write(int(k * gWidth))
	self.response.out.write(' stitches)')

	if size < 8:
            l = 1
        else:
            l = 2
	self.response.out.write('\nL:')
	self.response.out.write(l)
	self.response.out.write(' inches (')
	self.response.out.write(int(l * gHeight))
	self.response.out.write(' stitches)')

        if shape == 0 or shape == 2:
            m = sleeve[size] - l
        else:
            m = round((sleeve[size] - l)*2/3, 0)
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

	if shape == 1 or shape == 2:
            if size < 8:
                p = 1
            else:
                p = 2
            self.response.out.write('\nP:')
            self.response.out.write(p)
            self.response.out.write(' inches (')
            self.response.out.write(int(p * gHeight))
            self.response.out.write(' stitches)')

            if shape == 1:
                q = wrist[size]
            elif shape == 2:
                q = 1.1 * k
            self.response.out.write('\nQ:')
            self.response.out.write(q)
            self.response.out.write(' inches (')
            self.response.out.write(int(q * gWidth))
            self.response.out.write(' stitches)')

            if shape == 1:
                r = sleeve[size] - m - l
                self.response.out.write('\nR:')
                self.response.out.write(r)
                self.response.out.write(' inches (')
                self.response.out.write(int(r * gHeight))
                self.response.out.write(' stitches)')

            if shape == 2:
                t = 1.2 * b
                s = 1.2 * t
            elif shape == 1:
                s = b
            self.response.out.write('\nS:')
            self.response.out.write(s)
            self.response.out.write(' inches (')
            self.response.out.write(int(s * gWidth))
            self.response.out.write(' stitches)')

            if shape == 1:
                t = waist[size]
            self.response.out.write('\nT:')
            self.response.out.write(t)
            self.response.out.write(' inches (')
            self.response.out.write(int(t * gWidth))
            self.response.out.write(' stitches)')

	if shape == 0:
            sleeveArea = (k*l + m*(o+k)/2 + n*(o+i)/2)*2
            bodyArea = (b*c*2 + g*d + (e+f)*i*2 + g*(d+e) + i*f*2 + .2*g*d)
        elif shape == 1:
            sleeveArea = (q*r + m*(o+q)/2 + l*(q+k)/2 + n*(o+i)/2)*2
            bodyArea = (p*b + c*(t+b)/2 + d*(t+s)/2)*2 + g*e + i*f*2 + (e+f)*g + .2*g*e
        elif shape == 2:
            sleeveArea = n*(i+o) + m*(o+q) + l*(q+k)
            bodyArea = (b*p + c*(t+s)/2)*2 + (d+e+f)*2*i + (2*d+e+f)*s/2 + (2*i + h)*(d+e+f)
        totalArea = float(sleeveArea + bodyArea)
	yarn = totalArea * gauge
	self.response.out.write('\n\nAmount of yarn needed: ')
	self.response.out.write(round(yarn, 2))
	self.response.out.write(' yards')
        self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/print', Sweater)],
                              debug=True)
