from bs4 import BeautifulSoup
import urllib2


jobkey = raw_input("Job title/keyword: ")
region = raw_input("Country, province, or city: ")

url = "http://ca.indeed.com/jobs?q={0}&l={1}".format(jobkey, region)

file = open('urls.txt', 'a')

f = urllib2.urlopen(url)

soup = BeautifulSoup(f, 'lxml')
divs = soup.findAll("h2", { "class" : "jobtitle" })

for x in range (0,10):
    string1 = str(divs[x])
    sub_string = string1.split(' ')
    address = sub_string[5]
    address = address.translate(None, '"')
    address = address.lstrip('href=')
    file.write("http://ca.indeed.com"+address+'\n')

print"Script Successful"
file.close()
