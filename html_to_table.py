import lxml.html
import re
with open("thing.html","r") as f:
    html = lxml.html.fromstring(f.read())
tables = html.xpath("//table[position() =1]//table[position()=1]")

for table in tables:
    print [re.sub(r"\s+",' ',elem.text_content()) for elem in table.xpath("*")
