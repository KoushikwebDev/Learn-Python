class Video:
    def preview(self):
        return "Showing a video preview"


class Document:
    def preview(self):
        return "Showing Document preview"

v = Video()
d = Document()


# if method is available then it will execute it
def show_preview(obj):
    return obj.preview()

print(show_preview(v))


# anotehr example

class Course:
    def __init__(self, topics):
        self.topics = topics

    def __len__(self):
        return len(self.topics)

c = Course(["Python", "Java", "C++"])
print(len(c))  # 3

c1 = Course("Python")
print(len(c1))  # 6
        