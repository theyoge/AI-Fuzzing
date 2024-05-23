import subprocess
import random
import string
import sys


def random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(length))


def fuzz(target_binary, max_length=150):
    crash_inputs = []

    for length in range(1, max_length + 1):
        input_string = random_string(length)
        print(f"Testing with input length: {length}")
        try:
            result = subprocess.run(
                [target_binary],
                input=input_string.encode(),
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5
            )
        except subprocess.CalledProcessError as e:
            print(f"Input length {length} causing crash (exit code {e.returncode})\n")
            crash_inputs.appent((length, input_string, e.returncode))
        except subprocess.TimeoutExpired:
            print(f"Timeout expired for input length: {length}, potentially causing a hang. Logging input.")
            crash_inputs.append((length, input_string, "Timeout"))

    if crash_inputs:
        with open("crash_inputs.log", "w") as log_file:
            for length, input_data, code in crash_inputs:
                log_file.write(
                    f"Input length {length} causing crash (exit code {code}): {input_data}\n"
                )
        print("Crashes logged to crash_inputs.log")
    else:
        print("No crashes detected.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fuzz.py <target_binary>")
    else:
        target_binary = sys.argv[1]
        fuzz(target_binary)
