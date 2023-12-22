import os
from api import run

# Define color codes
W = '\033[0m'   # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

# Professional banner
def print_banner():
    print(B +
      "============================================================\n" +
      "                      Welcome to API 2.0.1\n" +
      "                      Version: 2.0.1\n"+
      "                      Author: Shiboshree Roy\n"+
      "                      Writer & Dev: Shiboshree Roy\n"+
      "============================================================" + W)

def run_api_repl():
    print_banner()

    # Specify the file path
    file_path = 'projects/calculetor.app'

    try:
        # Check if the file path ends with ".app"
        if not file_path.lower().endswith(".app"):
            raise ValueError(f"Invalid file extension. Expected '*.app', got '{file_path}'")

        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            print(f"Your Program:\n{content}")

            # Execute the content of the file
            result, error = run(R + f"<{file_path}>", content)
            if error:
                print(R + "Error: " + W + error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(G + "Result: " + W + repr(result.elements[0]))
                else:
                    print(G + "Result: " + W + repr(result))

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
    except ValueError as ve:
        print(f"Error: {ve}")

    while True:
        try:
            # Improved command prompt
            text = input(C + "API 2.0.1> " + W)

            if text.strip().lower() == "clear":
                os.system('clear' if os.name == 'posix' else 'cls')
                continue
            
            if not text.strip():
                continue

            # Execute the command
            result, error = run(R + "<stdin>", text)

            if error:
                # Display errors in red
                print(R + "Error: " + W + error.as_string())
            elif result:
                # Display results in green
                if len(result.elements) == 1:
                    print(G + "Result: " + W + repr(result.elements[0]))
                else:
                    print(G + "Result: " + W + repr(result))

        except KeyboardInterrupt:
            print(GR + '\nExiting API REPL.' + R + ' Goodbye!')
            break
        except Exception as e:
            print(R + f'An unexpected error occurred: {str(e)}')

if __name__ == "__main__":
    run_api_repl()
