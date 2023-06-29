class D3:
    def __init__(self):
        self._d3_str = "d3"

    def select(self, tag: str):
        if not str:
            raise ValueError("tag argument is empty")

        self._d3_str += f".select(\"{tag}\")"
        return self

    def append(self, svg_tag: str):
        if not str:
            raise ValueError(f"svg_tag argument is empty")
        self._d3_str += f".append(\"{svg_tag}\")"
        return self

    def attr(self, attr: str, value):
        if not attr:
            raise ValueError(f"attr argument is empty")
        self._d3_str += f".attr(\"{attr}\", {value})"
        return self

    def d3str(self):
        return self._d3_str

    def __str__(self):
        return self._d3_str

