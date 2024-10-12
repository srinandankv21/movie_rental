# app.py

import streamlit as st
from security_system import SecurityAgent, Person

# Create an instance of SecurityAgent
security_agent = SecurityAgent()

# Title of the application
st.title("Home Security System")

# Simulate capturing an image of a person
if st.button("Capture Image"):
    st.success(security_agent.capture_image())

# Input for a new person (e.g., a detected intruder)
person_id = st.text_input("Enter Person ID (e.g., '4' for an unknown person)")

if st.button("Check Person"):
    if person_id:
        # Create a new Person object for the detected individual
        unknown_person = Person(person_id)

        # Check if the person is in the known database
        known_person = security_agent.check_database(unknown_person)

        if known_person:
            st.write(f"{known_person.person_id} is known.")
        else:
            # If the person is unknown, notify the user and warn family/visitors
            st.write(f"{unknown_person.person_id} is an unknown person.")
            warning = security_agent.warn_family_and_visitors(unknown_person)
            st.warning(warning)

            # Notify the homeowner
            homeowner_alert = Homeowner.notify(unknown_person)
            st.info(homeowner_alert)

            # Simulate Jane confirming the identity
            jane_confirmation = Jane.confirm_identity(unknown_person)
            st.write(jane_confirmation)

            # Report to the police
            police_report = Police.report_incident(unknown_person)
            st.write(police_report)

            # Escalate alert to emergency services
            emergency_alert = EmergencyServices.escalate_alert(unknown_person)
            st.write(emergency_alert)
    else:
        st.error("Please enter a Person ID.")

# Display known family members and visitors
st.subheader("Known Family Members and Visitors")
for person in security_agent.known_people:
    st.write(f"- {person.person_id} ({'Family Member' if person.is_family_member else 'Visitor'})")
