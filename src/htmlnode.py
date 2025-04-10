

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ''
        for k in self.props:
            props_string += ' ' + str(k) + '="' + str(self.props[k]) + '"'
        return props_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props   

        
    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_string = ''
            for p in self.props:
                props_string += f' {p}="{self.props[p]}"'
                
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

