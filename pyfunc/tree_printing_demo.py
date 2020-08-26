
class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'
    
    
root = node('grandmother')
root.children = [node('daughter'), node('son')]
root.children[0].children = [node('granddaughter'), node('grandson')]
root.children[1].children = [node('granddaughter'), node('grandson')]
print root
