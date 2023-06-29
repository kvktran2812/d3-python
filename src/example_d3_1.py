import yfinance as yf
import webbrowser
import json
from bs4 import BeautifulSoup
from src.d3 import D3

html_text = str()

with open('test.html', 'r') as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
    body = soup.find('body')
    body.clear()
    new_tag = soup.new_tag("script")
    element = D3()
    element.select("body") \
        .append("svg") \
        .append("rect") \
        .attr("width", 100) \
        .attr("height", 100)
    new_tag.append(
        element.d3str()
    )
    body.append(new_tag)
    html_text = soup.prettify()

# print(html_text)
file = open('test.html', 'w')
file.write(html_text)
file.close()
webbrowser.open('test.html')

