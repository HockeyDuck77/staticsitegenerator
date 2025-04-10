import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('p', 'This is a test', None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        print(f'Children none: {node.props_to_html()}')

    def test_children(self):
        node = HTMLNode('p', 'Test Node 1', None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        node_2 = HTMLNode('p', None, node, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        print('Parent node: ' + node_2.__repr__())
        print('Child node: ' + node.__repr__())

    

if __name__ == "__main__":
    unittest.main()