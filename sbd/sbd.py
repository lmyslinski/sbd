from lxml import html
from bs4 import BeautifulSoup
import pdfkit
import re
import mechanize
import cookielib
import argparse
import os
import validators


def remove_non_ascii_chars(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text)


def get_credentials(arguments):
    if arguments.login is not None and arguments.password is not None:
        return arguments.login, arguments.password
    elif os.environ.has_key("SBD_LOGIN") and os.environ.has_key("SBD_PASSWORD"):
        return os.environ["SBD_LOGIN"], os.environ["SBD_PASSWORD"]
    else:
        print "You must provide Safari Books Online credentials"
        exit()


baseurl = 'https://www.safaribooksonline.com/'

parser = argparse.ArgumentParser(
    description='A small program to download books from Safari Books Online for offline storage.')
parser.add_argument('-u', '--login', help='Safari Books Online login')
parser.add_argument('-p', '--password', help='Safari Books Online password')
parser.add_argument('safari_book_url',
                    help='Safari book url, ex. https://www.safaribooksonline.com/library/view/book-name/book-code/')


def main():
    args = parser.parse_args()
    url = args.safari_book_url

    if not validators.url(url):
        print "URL is invalid, please pass proper URL"
        exit()

    login, password = get_credentials(args)

    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://www.safaribooksonline.com/accounts/login")
    br.select_form(nr=0)
    br.form['email'] = login
    br.form['password1'] = password
    response = br.submit()
    page = response.read()
    page_ascii_only = remove_non_ascii_chars(page)
    tree = html.fromstring(page_ascii_only)
    errorlist = tree.xpath('//*[@id="login-form"]/small/ul/li')

    if errorlist.__len__() != 0:
        print "Login has failed: " + errorlist[0].text
        exit()
    else:
        print "Login successful"

    page = br.open(url).read()
    page_ascii_only = remove_non_ascii_chars(page)
    tree = html.fromstring(page_ascii_only)

    urllist = []

    for atag in tree.xpath('//*[@class="detail-toc"]//li/a'):
        urllist.append(baseurl + atag.attrib['href'])

    title = tree.xpath('//*[@class="title t-title"]/text()')[0]
    author = tree.xpath('//*[@class="author t-author"]//a/text()')[0]
    author_title = author + ' - ' + title
    filename = str(author_title) + '.pdf'

    complete_book = ''
    print 'Downloading ' + author_title
    # fetch all the book pages
    for x in range(0, urllist.__len__()):
        print "Downloading chapter " + str(x + 1) + " out of " + str(urllist.__len__())
        bookpage = br.open(urllist[x]).read()
        bs = BeautifulSoup(remove_non_ascii_chars(bookpage), 'lxml')
        content = bs.find("div", {"id": "sbo-rt-content"})
        for img in content.findAll('img'):
            img['src'] = img['src'].replace("/library/", baseurl + "library/")
        complete_book += content.__str__()

    print "Generating pdf..."
    pdfkit.from_string(complete_book, filename, options=dict(encoding="utf-8", quiet=''))
    print("Done! Saved as '" + filename + "'")
