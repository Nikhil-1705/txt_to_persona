import warnings
from datetime import datetime
from txtpersona.crew import Txtpersona
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the Txtpersona crew to process user data and generate structured user personas.
    """
    inputs = {
        'file_path': 'users.txt',  # Ensure this file exists in the correct directory
        'current_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    try:
        persona_crew = Txtpersona().crew()
        persona_crew.kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
