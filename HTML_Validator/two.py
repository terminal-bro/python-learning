from bs4 import BeautifulSoup, NavigableString, Tag 

text = """<html lang="en">
<body class="outline narrow">
<p align="left" align="right">paragraph</p>
</body>
</html>"""

doc = BeautifulSoup(text, "html.parser")

def display(node):
    if isinstance(node, NavigableString):
        print(f"string : {repr(node.string)}")
        return
    else:
        print(f"Node : {node.name} {node.attrs}")
        for child in node:
            display(child)
display(doc)