import pycurl
from datetime import datetime, timedelta
from datetime import datetime

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# As long as the file is opened in binary mode, both Python 2 and Python 3
# can write response body to it without decoding.
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?"now"&i=wiii')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))


with open('visibility.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=4&y=2021&i=wiii')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('finish, save.txt')




