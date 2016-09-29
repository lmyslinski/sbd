import mechanize
import cookielib


def login():
    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://www.safaribooksonline.com/accounts/login")

    br.select_form(nr=0)
    br.form['email'] = 'dejtabejz@gmail.com'
    br.form['password1'] = 'th3wa11y'
    br.submit()
    return br