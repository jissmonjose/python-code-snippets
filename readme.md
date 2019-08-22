# Python Challenges For Practice

**Problems**
____________

1. Electronics Shop 

    [Problem Description](https://www.hackerrank.com/challenges/electronics-shop/problem)

2. Bon Appetit 

    [Problem Description](https://www.hackerrank.com/challenges/bon-appetit/problem)

3. Cat and Mouse

    [Problem Description](https://www.hackerrank.com/challenges/cats-and-a-mouse/problem)
    
4. Breaking the Records
    
    [Problem Description](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem)

5. The Hurdles Race

    [Problem Description ](https://www.hackerrank.com/challenges/the-hurdle-race/problem)
______________

### Web Scraping

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





