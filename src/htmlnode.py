

class HTMLNODE:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    # def props_to_html(self):
    #     href = self.props["href"]
    #     target = self.props.get("target")
    #     return f' href="{href}"' + (f' target="{target}"' if target else "")
    #     #return f' href={self.props["href"]} target={self.props["target"]}'

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
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        # if self.tag == 'a':
        #     return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        # return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        class_name = self.__class__.__name__
        props_value = ", ".join(f"{key}: {value}" for key, value in self.props.items()) if self.props else None
        return f"{class_name}({self.tag}, {self.value}, {props_value})"

        