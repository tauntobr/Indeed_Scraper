#Indeed_Scraper v1.0 by tauntobr (Benjamin Taunton). 
#Created August 23 2015 using Python 2.7.10, BeautifulSoup 4 and lxml 3.4.4
#This program asks the user to input a job title or keyword and a geographic region (ie city, province/state, country)
#The program outputs a single .txt file containing the urls returned by the search query on Indeed.com. 
#Currently returns only the first page of results.

from bs4 import BeautifulSoup
import urllib2


jobkey = raw_input("Job title/keyword: ") #Get the job title/keyword input from user as string
region = raw_input("Country, province, or city: ") #Get the geographic region from user as string

url = "http://ca.indeed.com/jobs?q={0}&l={1}".format(jobkey, region) #create the url, including the search terms

file = open('urls.txt', 'a') #open/create the .txt file to contain the result urls

f = urllib2.urlopen(url) #open the completed url

soup = BeautifulSoup(f, 'lxml') #get and parse the resulting indeed.com result page
divs = soup.findAll("h2", { "class" : "jobtitle" }) #find all <h2> tags containing the glass called "jobtitle"

#loop through the results, grab the href, strip unnecessary characters and place the information into a complete url
#then write the resulting url to file
for x in range (0,10):
    string1 = str(divs[x])
    sub_string = string1.split(' ')
    address = sub_string[5]
    address = address.translate(None, '"')
    address = address.lstrip('href=')
    file.write("http://ca.indeed.com"+address+'\n')

print"Script Successful" #let user know the program ran successfully
file.close() #close the file
