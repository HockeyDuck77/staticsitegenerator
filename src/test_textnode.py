import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("Test1", TextType.NORMAL, 'https://www.boot.dev')
        node2 = TextNode("Test2", TextType.NORMAL, 'https://www.boot.dev')
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Test1", TextType.NORMAL, 'https://www.boot.dev')
        node2 = TextNode("Test1", TextType.BOLD, 'https://www.boot.dev')
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("Test1", TextType.NORMAL, 'https://www.boot.dev')
        node2 = TextNode("Test1", TextType.NORMAL, 'https://www.python.com')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
