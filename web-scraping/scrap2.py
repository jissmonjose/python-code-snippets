from bs4 import BeautifulSoup
import requests
from csv import writer

head5 = list()

course_name = None

syllabus_lst = list()


def scrap(url):
    global course_name, head5
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    div_items = soup.find_all('div', class_="single-item-text")
    with open('./csv-files/courses.csv', 'w') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['courses'])
        for each_div in div_items:
            # fetch course names
            new_lst = each_div.find('strong').text
            new_lst.strip("")
            # print(new_lst)
            print(new_lst)
            csv_writer.writerow([new_lst])


scrap('http://www.luminartechnolab.com/course.html')
