import argparse
import os
import pdfkit
import re
import validators
from robobrowser import RoboBrowser


def remove_non_ascii_chars(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text)


def get_credentials(arguments):
    if arguments.login is not None and arguments.password is not None:
        return arguments.login, arguments.password
    elif os.environ["SBD_LOGIN"] and os.environ["SBD_PASSWORD"]:
        return os.environ["SBD_LOGIN"], os.environ["SBD_PASSWORD"]
    else:
        print("You must provide Safari Books Online credentials")
        exit()


base_url = 'https://www.safaribooksonline.com/'
login_url = 'https://www.safaribooksonline.com/accounts/login'

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
        print("URL is invalid, please pass proper URL")
        exit()

    login, password = get_credentials(args)

    br = RoboBrowser(parser='lxml')
    br.open(login_url)
    login_form = br.get_form()
    login_form['email'].value = login
    login_form['password1'].value = password
    br.session.headers['Referer'] = login_url
    br.submit_form(login_form)

    error_list = br.parsed.find_all("ul", class_='errorlist')

    if error_list.__len__() != 0:
        print("Login has failed: " + error_list[0].contents[0].text)
        exit()
    else:
        print("Login successful")

    br.open(url)
    url_list = []

    for chapter in br.parsed.find_all("a", class_='t-chapter'):
        url_list.append(base_url + chapter['href'])

    author = br.parsed.find('meta', {"property": 'og:book:author'})['content']
    title = br.parsed.find('meta', {"itemprop": 'name'})['content']
    author_title = author + ' - ' + title
    filename = str(author_title) + '.pdf'

    complete_book = ''
    print('Downloading ' + author_title)
    # fetch all the book pages
    for x in range(0, url_list.__len__()):
        print("Downloading chapter " + str(x + 1) + " out of " + str(url_list.__len__()))
        br.open(url_list[x])
        content = br.parsed.find("div", {"id": "sbo-rt-content"})
        for img in content.findAll('img'):
            img['src'] = img['src'].replace("/library/", base_url + "library/")
        complete_book += remove_non_ascii_chars(content.__str__())

    print("Generating pdf...")
    pdfkit.from_string(complete_book, filename, options=dict(encoding="utf-8", quiet=''))
    print("Done! Saved as '" + filename + "'")
