class StudentIterator:

    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.students):
            raise StopIteration

        student = self.students[self.index]
        self.index += 1

        return student