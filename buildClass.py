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
    classHeader = f"\npublic class {className} {{\n"

    with open(f"{OUTPUT_DIR}/{className}.java", "w+") as classFile:

        # Boiler Plate Code:
        classFile.write(jDocComment)
        classFile.write(classHeader)

        # Instance Variables:
        for iv in instanceVarList:
            classFile.write(f"\tprivate {iv['type']} {iv['name']};\n")

        classFile.write("\n\t// Constructors\n")

        # Constructors:
        constructorTemplate = f"\t{className}("
        for iv in instanceVarList[:-1]:
            constructorTemplate += f"{iv['type']} new{iv['name'].capitalize()},"

        iv2 = instanceVarList[-1]  # Last element
        constructorTemplate += f"{iv2['type']} new{iv2['name'].capitalize()}"
        constructorTemplate += ")\n\t{\n"

        for iv in instanceVarList:
            constructorTemplate += f"\t\t{iv['name']} = new{iv['name'].capitalize()};\n"

        constructorTemplate += "\t}\n"
        classFile.write(constructorTemplate)

        # End class
        classFile.write("}")


if __name__ == "__main__":
    main()
