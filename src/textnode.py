from enum import Enum
from htmlnode import HTMLNODE, LeafNode, ParentNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

    def textnode_to_htmlnode(self): #WIP
        if self.text_type not in {texttype.value for texttype in TextType}:
            raise Exception("unknown Text Type")
        if self.TextType.TEXT:
            return LeafNode(None, self.text)
        if self.TextType.BOLD:
            return LeafNode("b", self.text)
        if self.TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.TextType.CODE:
            return LeafNode("code", self.text)
        if self.TextType.LINK:
            return LeafNode("link", self.text, {"href": self.url})
        if self.TextType.IMAGE:
            return LeafNode("img", None, {"src":self.url, "alt": self.text})
        