import re

from lxml import html
import requests, pdfkit

def remove_non_ascii_chars(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text)

url = 'https://www.safaribooksonline.com/library/view/software-build-systems/9780132171953/'
baseurl = 'https://www.safaribooksonline.com/'

page = requests.get(url)

# get rid of non ascii characters
page_ascii_only = remove_non_ascii_chars(page.content)

tree = html.fromstring(page_ascii_only)

urllist = []

for atag in tree.xpath('//*[@id="toc"]/ol//li/a'):
    urllist.append(baseurl + atag.attrib['href'])


bookpages = []

#fetch all the book pages
#for entry in urllist:
entry = urllist[0]
bookpage = requests.get(entry)
bookpage_clean = remove_non_ascii_chars(bookpage.content)
bookpage_content = html.fromstring(bookpage_clean)
purebook = bookpage_content.xpath('//*[@id="sbo-rt-content"]')
bookpages.append(purebook)
#

print bookpage_content

#for x in range (0, urllist.__len__()):
x=0
pdfkit.from_string(bookpage_clean, 'test' + str(x) + '.pdf', options=dict(encoding="utf-8"))


