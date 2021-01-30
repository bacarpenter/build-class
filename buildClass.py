from rich import print

# Change me!
OUTPUT_DIR = "/Users/bencarpenter/Code/build-class/outputs"


def main():
    try:
        # Welcome
        print("[bold green]build-class[/bold green] | Ben Carpenter, 2021")
        print("---------------------------------")

        # Get info for build class
        className = input("Class name (CapitalAllWords): ")
        numberOfIV = int(input("How many instance variables: "))

        instanceVariables = []  # List of dicts of IV's

        i = 0
        while i < numberOfIV:
            instanceIn = input(
                f"Instance Variable #{i} (name:data_type): ").split(":")
            instanceName = instanceIn[0]
            instanceType = instanceIn[1]
            instanceVariables.append(
                {'name': instanceName, 'type': instanceType})
            i += 1
    except KeyboardInterrupt:
        print("\nGood Bye! 👋")
        exit(1)

    buildClass(className, instanceVariables)


def buildClass(className, instanceVarList):
    jDocComment = f"/**\n * {className} class built with the build-class python script\n * https://github.com/bacarpenter/build-class\n */"
    with open(f"{OUTPUT_DIR}/{className}.java", "w+") as classFile:
        classFile.write(jDocComment)


if __name__ == "__main__":
    main()
