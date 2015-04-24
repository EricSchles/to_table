# A simple html parser
# The data structure in question here is a b-Tree, 
# because the expectation is there will be many sub-elements to any given node.
# For an understanding of data structures in python, check out:

# http://www.openbookproject.net/thinkcs/python/english2e/index.html 

#this is more or less a B-tree
class HTMLNode:
    def __init__(self,tag,data='',children=[],parent=None):
        self.tag = tag
        self.data = data
        self.children = children
        self.parent = parent

    def set_children(self,children):
        self.children = children

    #reference to the parent node (there can be only one of these)
    def set_parent(self,parent):
        self.parent = parent

    def append_child(self,child):
        self.children.append(child)

    def __str__(self):
        return repr(self.data)


class Parser:
    def __init__(self,document=''):
        if "<!" in document:
            document = document.replace("<!doctype html","")  
        self.document = document.replace("\r","\n").replace("\n","")
        self.obj = self.transform(self.document)

    def traverse_exists(self,cur):
        pass
        
    def tag_exists(self,tag):
        pass
        # head = self.obj
        # cur = head
        # found = False
        # while not found:
        #     if cur.tag == tag:
        #         found = True
        #     else:
        #         for child in cur.children:
        #             if child.tag == tag:
        #                 found = True
        #             else:
        #                 while child:
                            


    #process html methods
    def transform(self,document):
        offset = document.find(">")
        if offset == -1:
            return HTMLNode(None,data=document)
        else:
            open_tag,close_tag,offset = self.find_tags(document)
            head = HTMLNode(open_tag,data=self.find_data(document),children=[])
            document = self.strip_doc(document,open_tag,close_tag)
            return self.dp_transform(document,head)

    def find_tags(self,document):
        offset = document.find(">")
        open_tag = document[:offset]+">"
        if "<" in open_tag: 
            close_tag = "</"+ open_tag.split("<")[1]
            return open_tag,close_tag,offset
        else:
            return "","",""

    def cut(self,document,tag):
        start = document.find(tag)
        end = document[start:].find(">")+1
        return document[:start]+document[start+end:]


    def find_data(self,document):
        offset = document.find(">")
        return document[offset:document[offset:].find("<")]
    
    def strip_doc(self,document,open_tag,close_tag):
        document = self.cut(document,open_tag)
        document = self.cut(document,close_tag)
        return document

    #recursive - maybe more complete
    def _transform(self,document,previous,head,count):
        print count
        open_tag,close_tag,offset = self.find_tags(document)
        current = HTMLNode(open_tag,data=self.find_data(document),children=[],parent=previous)
        #sets reference so that child and parent nodes are linked
        previous.append_child(current)
        document = self.strip_doc(document,open_tag,close_tag)
        if offset == -1 or document == '' or open_tag==None or close_tag==None:
            return head
        else:
            return self._transform(document,current,head,count+1)
    

    #iterative (dynamic programming) - possibly misses some cases, more testing required here
    def dp_transform(self,document,head,offset=0,open_tag='',close_tag=''):
        count = 0
        previous = head
        while offset != -1 or document != '' or open_tag!='' or close_tag!="":
            #print offset
            open_tag,close_tag,offset = self.find_tags(document)
            print document
            if open_tag == '':
                break
            current = HTMLNode(open_tag,data=self.find_data(document),children=[],parent=previous)
            #sets reference so that child and parent nodes are linked
            previous.append_child(current)
            document = self.strip_doc(document,open_tag,close_tag)
            count += 1
            previous = current
        return head


    def __str__(self):
        return repr(self.obj)

if __name__ == '__main__':
    with open("test.html","r") as f:
        obj = Parser(document=f.read())
    print obj
