class Section:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"Section Title: {self.title}")
        print(f"Content: {self.content}")

section1 = Section("Introduction", "This is the introduction section.")
section1.display()

