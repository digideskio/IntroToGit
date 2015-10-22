import random
import os

def generate_random_names(count):
    first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
    last_names = ["Smith", "Jones", "Brighton", "Taylor"]
    for filename in os.listdir(os.path.join(os.getcwd(), "names")):
        split_names = filename.split()
        first_names.append(split_names[0])
        last_names.append(split_names[1])
    output_names = []
    for i in range(count - 1):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        output_names.append(first_name + " " + last_name)
    return output_names

if __name__ == "__main__":
    print generate_random_names(10)
