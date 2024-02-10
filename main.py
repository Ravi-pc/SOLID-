# # 1. Single Responsibility Principle
# The Single Responsibility Principle states that a class should do
# one thing, and therefore it should have only a single reason to change.


class EmailService:
    def __init__(self, logger):
        self.logger = logger

    def send_email(self, to_address, subject, message):
        # Code for sending email
        # Log email activity
        self.logger.log(f"Email sent to {to_address}: {subject}")


class Logger:
    def log(self, message):
        # Code for logging message
        pass


# 2. Open-Closed Principle
# The Open-Closed Principle requires that classes should be open for extension
# and closed to modification.
# Modification means changing the code of an existing class,
# and extension means adding new functionality.
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# Liskov Substitution Principle
# The Liskov Substitution Principle states that subclasses should be substitutable
# for their base classes.


class Bird:
    def fly(self):
        pass


class Duck(Bird):
    def fly(self):
        print("Duck flying")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


# Interface Segregation Principle
# Segregation means keeping things separated, and the Interface Segregation Principle is
# about separating the interfaces.
# The principle states that many client-specific interfaces are better than
# one general-purpose interface. Clients should not be forced to implement a function they do no need.

class DocumentPrinter:
    def print_document(self, document):
        pass


class PhotoPrinter:
    def print_photo(self, photo):
        pass


class Document:
    def __init__(self, content):
        self.content = content


class Photograph:
    def __init__(self, image):
        self.image = image


class SimpleDocumentPrinter(DocumentPrinter):
    def print_document(self, document):
        print("Printing document:", document.content)


class SimplePhotoPrinter(PhotoPrinter):
    def print_photo(self, photo):
        print("Printing photograph:", photo.image)


# 5.The Dependency Inversion Principle (DIP) is one of the SOLID principles of object-oriented
# design, and it states that high-level modules should not depend on low-level modules.
# Both should depend on abstractions. In addition, abstractions should not depend on details;
# rather, details should depend on abstractions.


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class SQLDatabase(Database):
    def save(self, data):
        print("Saving data to SQL database")


class NoSQLDatabase(Database):
    def save(self, data):
        print("Saving data to NoSQL database")


class BusinessLogic:
    def __init__(self, database):
        self.database = database

    def process_data(self, data):
        # Do some business logic processing
        self.database.save(data)
