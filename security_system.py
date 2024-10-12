# security_system.py

from datetime import datetime

class Person:
    def __init__(self, person_id):
        self.person_id = person_id
        self.is_family_member = False
        self.is_visitor = False

class FamilyMember(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id)
        self.name = name
        self.is_family_member = True

class Visitor(Person):
    def __init__(self, person_id, name, scheduled_time):
        super().__init__(person_id)
        self.name = name
        self.scheduled_time = scheduled_time
        self.is_visitor = True

class SecurityAgent:
    def __init__(self):
        self.known_people = []

    def capture_image(self):
        return "Image captured."

    def check_database(self, person):
        for known_person in self.known_people:
            if known_person.person_id == person.person_id:
                return known_person
        return None

    def warn_family_and_visitors(self, unknown_person):
        return f"Warning: Unknown person detected - {unknown_person.person_id}"

class Jane:
    @staticmethod
    def confirm_identity(person):
        return f"Jane is confirming the identity of {person.person_id}."

class Homeowner:
    @staticmethod
    def notify(unknown_person):
        return f"Homeowner notified about unknown person: {unknown_person.person_id}"

class Police:
    @staticmethod
    def report_incident(unknown_person):
        return f"Reported incident of unknown person: {unknown_person.person_id}"

class EmergencyServices:
    @staticmethod
    def escalate_alert(unknown_person):
        return f"Alert escalated to Emergency Services for {unknown_person.person_id}."

# Sample known people for demonstration
known_family = [
    FamilyMember("1", "Alice"),
    FamilyMember("2", "Bob")
]

known_visitors = [
    Visitor("3", "Charlie", datetime.now())
]

security_agent = SecurityAgent()
security_agent.known_people.extend(known_family + known_visitors)
