

class HTMLNODE:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        class_name = self.__class__.__name__
        children_value = self.children.value if self.children else None
        props_value = ", ".join(f"{key}: {value}" for key, value in self.props.items()) if self.props else None
        return f"{class_name}({self.tag}, {self.value}, {children_value}, {props_value})"


class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == "img":
            return f'<{self.tag}{self.props_to_html()}/>'
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        class_name = self.__class__.__name__
        props_value = ", ".join(f"{key}: {value}" for key, value in self.props.items()) if self.props else None
        return f"{class_name}({self.tag}, {self.value}, {props_value})"


class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: missing children")
        content = ""
        for child in self.children:
            content += child.to_html()
        return f'<{self.tag}>{content}</{self.tag}>'


    def __repr__(self):
        class_name = self.__class__.__name__
        props_value = ", ".join(f"{key}: {value}" for key, value in self.props.items()) if self.props else None
        return f"{class_name}({self.tag}, {self.children}, {props_value})"

