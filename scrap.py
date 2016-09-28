import re

from lxml import html
import requests, pdfkit

url = 'https://www.safaribooksonline.com/library/view/software-build-systems/9780132171953/'

page = requests.get(url)

# get rid of non ascii characters
page_ascii_only = re.sub(r'[^\x00-\x7F]+', ' ', page.content)

tree = html.fromstring(page_ascii_only)

table_of_content = tree.xpath('//*[@id="toc"]')
print table_of_content

#pdfkit.from_string(page_ascii_only, 'out.pdf', options=dict(encoding="utf-8"))
