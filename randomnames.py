import random

def generate_random_names(count):
    first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
    last_names = ["Smith", "Jones", "Brighton", "Taylor"]
    output_names = []
    for i in range(count):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        output_names.append(first_name + " " + last_name)
    return output_names

if __name__ == "__main__":
    print generate_random_names(10)
