import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_with_two_children(self):
        child_node1 = LeafNode("b", "child one")
        child_node2 = LeafNode("span", "child two")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child one</b><span>child two</span></div>",
    )



if __name__ == "__main__":
    unittest.main()