


import requests
import bs4


http://books.toscrape.com/catalogue/page-2.html


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


page_num = 12
base_url.format(page_num)


res = requests.get(base_url.format(1))


soup = bs4.BeautifulSoup(res.text,'lxml')


soup.select(".product_pod")


products = soup.select(".product_pod")


example = products[0]


example.select(".star-rating.Three") #use dot in the space here


example.select('a') # we find the <a part and put that in


example.select('a')[1]['title']


#we can check if something is 2 stars (string call in, exaple.select(rating))
#example.select('a')[1]['title'] to grab book title



two_star_titles = []

for n in range (1,51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

    return two_star_titles



