# A simple html parser
# The data structure in question here is a b-Tree, 
# because the expectation is there will be many sub-elements to any given node.
# For an understanding of data structures in python, check out:

# http://www.openbookproject.net/thinkcs/python/english2e/index.html 

class HTMLNode:
    def __init__(self,tag,data='',children=[]):
        self.tag = tag
        self.data = data
        self.children = children

    def set_children(self,children):
        self.children = children

    def append_child(self,child):
        self.children.append(child)

    def __str__(self):
        return repr(self.data)


class Parser:
    def __init__(self,document):
        self.document = document
        self.obj = self.transform(self.document)

    def transform(self,document):
        offset = document.find(">")
        if offset == -1:
            return HTMLNode(None,data=document)
        else:
            open_tag,close_tag,offset = self.find_tags(document)
            head = HTMLNode(open_tag,data=self.find_data(document),children=[])
            document = self.strip_doc(document,open_tag,close_tag)
            return self._transform(document,head)

    def find_tags(self,document):
        offset = document.find(">")
        open_tag = document[:offset]+">"
        close_tag = "</"+ open_tag.split("<")[1]
        return open_tag,close_tag, offset

    def find_data(self,document):
        offset = document.find(">")
        return document[offset:document[offset:].find("<")]
    
    def strip_doc(self,document,open_tag,close_tag):
        return "<"+document.lstrip(open_tag).rstrip(close_tag)+">"
        
    def _transform(self,document,head):
        offset = document.find(">")
        if offset == -1:
            return 
        return head



    def __str__(self):
        return repr(self.obj)
