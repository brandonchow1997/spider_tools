import selenium_general


def main():
    url = 'https://brandonchow1997.github.io/'
    browser = selenium_general.initial_browser()
    html = selenium_general.no_login(browser, url)
    print(html)


if __name__ == '__main__':
    main()