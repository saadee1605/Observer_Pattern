# Observer Interface
class Observer:
    def update(self, student_name, grade):
        raise NotImplementedError

# Subject Class
class GradeBook:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, student_name, grade):
        for observer in self._observers:
            observer.update(student_name, grade)

    def enter_grade(self, student_name, grade):
        print(f"Grade entered: {student_name} - {grade}")
        self.notify_observers(student_name, grade)

# Concrete Observer: Parent Portal
class ParentPortal(Observer):
    def update(self, student_name, grade):
        print(f"[Parent Portal] {student_name} received a grade of {grade}.")

# Concrete Observer: Student Portal
class StudentPortal(Observer):
    def update(self, student_name, grade):
        print(f"[Student Portal] Hello {student_name}, your new grade is {grade}.")

# Concrete Observer: Analytics Dashboard
class AnalyticsDashboard(Observer):
    def update(self, student_name, grade):
        print(f"[Analytics Dashboard] Logging: {student_name} got {grade}.")

# Usage
if __name__ == "__main__":
    gradebook = GradeBook()

    parent = ParentPortal()
    student = StudentPortal()
    dashboard = AnalyticsDashboard()

    gradebook.add_observer(parent)
    gradebook.add_observer(student)
    gradebook.add_observer(dashboard)

    gradebook.enter_grade("Alice", 92)
    gradebook.enter_grade("Bob", 85)
