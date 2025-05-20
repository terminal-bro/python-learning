from bs4 import BeautifulSoup, NavigableString, Tag 

text = """<html>
<body>
<h1>Title</h1>
<p>paragraph</p>
</body>
</html>"""

doc = BeautifulSoup(text, "html.parser")

def display(node):
    if isinstance(node, NavigableString):
        print(f"string : {repr(node.string)}")
        return
    else:
        print(f"Node : {node.name}")
        for child in node:
            display(child)
display(doc)