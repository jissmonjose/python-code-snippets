# Python Challenges For Practice

**Problems**
____________

1. Electronics Shop 

    [Problem Description](https://www.hackerrank.com/challenges/electronics-shop/problem)

2. Bon Appetit 

    [Problem Description](https://www.hackerrank.com/challenges/bon-appetit/problem)
__________________

### Web Scraping
---------------
web scraping using BeautifulSoup library.

**Installation**
-----------------
Using `pip`,
```bash
pip install BeautifulSoup
pip install lxml
```
*To parse a document, pass it into the ```BeautifulSoup``` constructor.*

```python
from bs4 import BeautifulSoup

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
print(soup)
```
---





