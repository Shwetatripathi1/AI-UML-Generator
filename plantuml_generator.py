# Function to generate PlantUML class diagram

def generate_plantuml(classes):

    uml_text = "@startuml\n"

    # Create class blocks
    for c in classes:
        uml_text += f"class {c} {{}}\n"

    uml_text += "@enduml"

    # Save UML file
    with open("output/diagram.puml", "w") as f:
        f.write(uml_text)

    return uml_text
