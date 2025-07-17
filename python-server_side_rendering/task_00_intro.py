import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input types. Template must be a string and attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with attendee data or "N/A" if missing
            invitation = template.replace("{name}", attendee.get("name", "N/A"))
            invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
            invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A"))
            invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

            # Generate output file
            output_filename = f"output_{index}.txt"
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)

        except Exception as e:
            print(f"An error occurred while processing attendee {index}: {e}")

# Example usage
if __name__ == "__main__":
    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
