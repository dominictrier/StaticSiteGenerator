

class HTMLNODE:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f' href={self.props["href"]} target={self.props["target"]}'
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        children_value = self.children.value if self.children else None
        props_value = ", ".join(f"{key}: {value}" for key, value in self.props.items()) if self.props else None
        return f"HTMLNODE({self.tag}, {self.value}, {children_value}, {props_value})"
    

class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.tag == "a":
            
        
        