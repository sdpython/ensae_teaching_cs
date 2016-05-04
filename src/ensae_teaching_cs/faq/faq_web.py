# -*- coding: utf-8 -*-
"""
@file
@brief A few functions about scrapping

"""
import os
import datetime


def webshot(img, url, navigator="firefox", add_date=False,
            module="selenium", size=None):
    """
    Uses the modules `selenium <http://selenium-python.readthedocs.io/>`_ to take a picture of a website
    (or the module `splinter <http://splinter.readthedocs.io/en/latest/>`_ - does not work with IE).
    The function was only tested with Firefox.
    If url and img are lists, the function goes through all the urls and save webshots.

    @param      img             list of image names
    @param      url             url
    @param      navigator       firefox, chrome, (ie: does not work well)
    @param      add_date        add a date to the image filename
    @param      module          module to use (selenium or splinter or None if you need to keep the first one available)
    @param      size            to resize the webshot (if not None)
    @return                     list of [ ( url, image name) ]

    Check the list of available webdriver at
    `selenium/webdriver <https://github.com/SeleniumHQ/selenium/tree/master/py/selenium/webdriver>`_
    and add one to the code if needed.
    """
    if navigator is None:
        try:
            import selenium as skip_
            module = "selenium"
        except ImportError:
            module = "splinter"

    res = []
    if module == "selenium":
        from selenium import webdriver

        if navigator == "firefox":
            browser = webdriver.Firefox()
        elif navigator == "chrome":
            browser = webdriver.Chrome()
        elif navigator == "ie":
            browser = webdriver.Ie()
        elif navigator == "edge":
            browser = webdriver.Edge()
        else:
            raise Exception("unable to interpret the navigator")

        if size is not None:
            browser.set_window_size(size[0], size[1])

        if not isinstance(url, list):
            url = [url]
        if not isinstance(img, list):
            img = [img]
        if len(url) != len(img):
            raise Exception("different number of urls and images")
        for u, i in zip(url, img):
            browser.get(u)
            if add_date:
                dt = datetime.datetime.now()
                a, b = os.path.splitext(i)
                i = "{0}.{1}{2}".format(a, str(dt).replace(
                    ":", "-").replace("/", "-"), b)
            browser.get_screenshot_as_file(i)
            res.append((u, i))
        browser.quit()

    elif module == "splinter":

        from splinter import Browser

        with Browser(navigator) as browser:
            if size is not None:
                browser.driver.set_window_size(size[0], size[1])

            if not isinstance(url, list):
                url = [url]
            if not isinstance(img, list):
                img = [img]
            if len(url) != len(img):
                raise Exception("different number of urls and images")
            for u, i in zip(url, img):
                browser.visit(u)
                if add_date:
                    dt = datetime.datetime.now()
                    a, b = os.path.splitext(i)
                    i = "{0}.{1}{2}".format(a, str(dt).replace(
                        ":", "-").replace("/", "-"), b)
                g = browser.screenshot(os.path.abspath(i))
                res.append((u, g))
    else:
        raise ImportError("unknown module required '{0}'".format(module))

    return res


def webhtml(url, navigator="firefox", module="selenium"):
    """
    Uses the modules `selenium <http://selenium-python.readthedocs.io/>`_ to retrieve the html of a website
    (or the module `splinter <http://splinter.readthedocs.io/en/latest/>`_ - does not work with IE).
    The function was only tested with Firefox.

    @param      url             url
    @param      navigator       firefox, chrome, (ie: does not work well)
    @param      module          module to use (selenium or splinter or None if you need to keep the first one available)
    @return                     list of [ ( url, html) ]

    Check the list of available webdriver at
    `selenium/webdriver <https://github.com/SeleniumHQ/selenium/tree/master/py/selenium/webdriver>`_
    and add one to the code if needed.
    """
    if navigator is None:
        try:
            import selenium as skip_
            module = "selenium"
        except ImportError:
            module = "splinter"

    res = []
    if module == "selenium":
        from selenium import webdriver

        if navigator == "firefox":
            browser = webdriver.Firefox()
        elif navigator == "chrome":
            browser = webdriver.Chrome()
        elif navigator == "ie":
            browser = webdriver.Ie()
        elif navigator == "edge":
            browser = webdriver.Edge()
        else:
            raise Exception("unable to interpret the navigator")

        if not isinstance(url, list):
            url = [url]
        for u in url:
            browser.get(u)
            i = browser.page_source
            res.append((u, i))
        browser.quit()

    elif module == "splinter":

        from splinter import Browser

        with Browser(navigator) as browser:
            if not isinstance(url, list):
                url = [url]
            for u in url:
                browser.visit(u)
                i = browser.html
                res.append((u, i))
    else:
        raise ImportError("unknown module required '{0}'".format(module))

    return res
