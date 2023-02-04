import urllib
import urllib2
import os
import time
import random
import codecs
import mechanize
import googlemaps

static_google_maps = None


def get_page_html(url, param):

    MechBrowser = mechanize.Browser()
    LoginUrl = url
    LoginData = param  # username=shane&password=123456&do=login"
    LoginHeader = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    LoginRequest = urllib2.Request(LoginUrl, LoginData, LoginHeader)
    LoginResponse = MechBrowser.open(LoginRequest)
    text = LoginResponse.read()
    #LoginRequest.close ()
    return text


def get_distance_ville(v1, v2, engine):
    global static_google_maps
    file = "memory\\html_%s_%s_%s.html" % (engine, v1, v2)
    if os.path.exists(file):
        f = codecs.open(file, "r", "utf-8")
        r = f.read()
        f.close()
        return r
    else:
        if engine == "mappy":
            url = "http://fr.mappy.com/itinerary_homepage#d%5B%5D=#V1#,+France&d%5B%5D=#V2#,+France&ipo=1&lm=r&p=itinerary"
            url = url.replace("#V1#", v1)
            url = url.replace("#V2#", v2)
            param = ""
            r = get_page_html(url, param)
        elif engine == "cara":
            url = "http://www.caradisiac.com/service/itineraire/"
            param = "iti-start-way=&iti-start-postal_code=&iti-start-town=%s&iti-start-country_code=France&iti-end-way=&iti-end-postal_code=&iti-end-town=%s&iti-end-country_code=France"
            param = param % (v1.lower(), v2.lower())
            r = get_page_html(url, param)
        elif engine == "googlemaps":
            h = random.randint(100, 200) * 1.0 / 1000
            time.sleep(h)
            if static_google_maps == None:
                static_google_maps = googlemaps.GoogleMaps(
                    api_key="ABQIAAAA3LCD_QWHgQyYWMUdx1mKtRTOLnapKzarYQ7apQ46S420-wKw2BQiR10GuPti7gX9-PpvG3ttFYn4Uw")
            try:
                x = static_google_maps.directions(v1, v2)
            except googlemaps.GoogleMapsError, e:
                raise RuntimeError("unable to get direction for " +
                                v1 + "," + v2 + "\n" + str(e))
            r = str(x)
        else:
            raise RuntimeError("choose an engine in [ mappy, cara, googlemaps ]")

        rl = r.lower()
        if v1.lower() not in rl or v2.lower() not in rl:
            raise RuntimeError(
                "unable to find cities from url\n" + url + "\n" + r)

        f = codecs.open(file, "w", "utf-8")
        f.write(r)
        f.close()
        return r


def get_html_for_everything(villes, engine):
    for i, v in enumerate(villes):
        print i, v
        for vv in villes:
            if v == vv:
                continue
            li = [v, vv]
            li.sort()
            try:
                t = get_distance_ville(li[0], li[1], engine)
            except:
                print "     unable for ", v, vv

if __name__ == "__main__":

    villes = [_.strip("\n\r\t ") for _ in open(
        "villes.txt", "r").readlines() if len(_) > 2]
    villes.sort()
    print villes
    get_html_for_everything(villes, "googlemaps")
