import lxml.html
from sys import argv
import pandas as pd

def main(html_page=None):
    data = head_body(html_page)
    if data["body"] != []:
        if data["head"]  != []:
            df = pd.DataFrame(columns=data["head"])
        else:
            df = pd.DataFrame()
    #df = df.

def head_body(html_page=None):
    html = lxml.html.fromstring(html_page)
    if html.xpath("//table") != []:
        headers = []
        body = []
        table_list = []
        
        for table in :
            print table.xpath("/")
            #print [elem.text_content().strip() for elem in table.xpath("/thead")]
            tmp_headers = [elem.text_content().strip() for elem in table.xpath("/th")]
            tmp_body = [elem.text_content().strip() for elem in table.xpath("//td")]
            # body = []
            # tmp = {}
            # counter = 0
            # for ind,elem in enumerate(tmp_body):
            #     if ind%len(headers)==0 and tmp != {}:
            #         counter = 0
            #         body.append(tmp)
            #         tmp = {}
            #         tmp[headers[counter]] = elem
            #         counter += 1
            # body.append(tmp)
            table_list.append({"head":headers,"body":body})

        return table_list
    else:
        return {"head":[],"body":[]}

if __name__ == '__main__':
    with open(argv[1],"r") as f:
        head_body(html_page=f.read())
