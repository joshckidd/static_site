import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_single_prop(self):
        node2 = HTMLNode("a", "link text", [], {"href": "http://www.test.com/"})
        self.assertEqual(node2.props_to_html(), " href=\"http://www.test.com/\"")

    def test_not_eq(self):
        node = HTMLNode("p", "paragraph text")
        node2 = HTMLNode("h1", "heading text")
        self.assertNotEqual(node, node2)

    def test_two_props(self):
        node2 = HTMLNode("a", "link text", [], {"href": "http://www.test.com/", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), " href=\"http://www.test.com/\" target=\"_blank\"")

class TestLeafNode(unittest.TestCase):
    def test_single_prop(self):
        node2 = LeafNode("a", "link text", {"href": "http://www.test.com/"})
        self.assertEqual(node2.props_to_html(), " href=\"http://www.test.com/\"")

    def test_not_eq(self):
        node = LeafNode("p", "paragraph text")
        node2 = LeafNode("h1", "heading text")
        self.assertNotEqual(node, node2)

    def test_two_props(self):
        node2 = LeafNode("a", "link text", {"href": "http://www.test.com/", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), " href=\"http://www.test.com/\" target=\"_blank\"")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()