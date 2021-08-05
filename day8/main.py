def greet():
    print("hello")
    print("how do you do")

greet()


def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}")

greet_with_name("angela")

def greet_with(name, location):
    print(f"hello {name}")
    print(f"{name} lives in {location}")

greet_with("jack", "london")