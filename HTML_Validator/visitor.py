from bs4 import BeautifulSoup, NavigableString, Tag 

text = """<html>
<body>
<h1>Title</h1>
<p>paragraph</p>
</body>
</html>"""

doc = BeautifulSoup(text, "html.parser")

class Visitor:

    def visit(self,node):
        if isinstance(node, NavigableString):
            self._text(node)
        elif isinstance(node, Tag):
            self._tag_enter(node)
            for child in node:
                self.visit(child)
            self._tag_exit(node)
        
    def _tag_enter(self,node): pass
    def _tag_exit(self, node): pass
    def _text(self, node): pass 

class Catalog(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.catalog = {}

    def _tag_enter(self,node):
        if node.name not in self.catalog:
            self.catalog[node.name] = set()
        for child in node:
            if isinstance(child, Tag):
                self.catalog[node.name].add(child.name)

cataloger = Catalog()
cataloger.visit(doc.html)
result = cataloger.catalog

print(result)