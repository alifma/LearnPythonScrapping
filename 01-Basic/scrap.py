# Importing library
from bs4 import BeautifulSoup

# Use local file, and only use it for read access
with open("home.html", "r") as html_file:
    #  read the content
     content = html_file.read()

     soup = BeautifulSoup(content, 'lxml')
    #  find and stop at the first element
    #  tag = soup.find('h5')

    # # Find everything that has 'h5'
    #  course_html_tags = soup.find_all('h5')

    # # Loop for everything found on course_html_tags
    #  for course in course_html_tags:
    #       print(course.text)

    # Find using tags and class
     course_tags = soup.find_all('div', class_='card')
     for course in course_tags:
          course_name = course.h5.text
          course_price = course.a.text.split()[-1]
          print(f'{course_name} is {course_price}')
