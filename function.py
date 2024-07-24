# controller class
class Person(Document):
    def get_full_name(self):
        """Returns the person's full name"""
        return f"{self.first_name} {self.last_name}"

# somewhere in your code
doc = frappe.get_doc("Person", "000001")
doc.get_full_name()

