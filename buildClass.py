from rich import print

# Change me to where you want your outputs to go.
OUTPUT_DIR = "/Users/bencarpenter/Scripts/build-class/outputs"

# List of dataType shortcuts. Feel free to change!
dataTypeShortcuts = [
    {
        "key": "i", "type": "int"
    },
    {
        "key": "s", "type": "String"
    },
    {
        "key": "d", "type": "double"
    },
    {
        "key": "b", "type": "boolean"
    }
]


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
            for dt in dataTypeShortcuts:
                if instanceType == dt['key']:
                    instanceType = dt['type']

            instanceVariables.append(
                {'name': instanceName, 'type': instanceType})
            i += 1
    except KeyboardInterrupt:
        print("\nGood Bye! 👋")
        exit(1)

    # ☺️ I like this line.
    includeSetters = not (input("Include setter methods (Y/n)? ") == "n")
    buildClass(className, instanceVariables, includeSetters)
    print(
        f"[bold]Built {className}:[/bold] {OUTPUT_DIR}/outputs/{className}.java")


def buildClass(className, instanceVarList, includeSetters):
    jDocComment = f"/**\n * {className} class built with the build-class python script\n * https://github.com/bacarpenter/build-class\n */\n"
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
            constructorTemplate += f"{iv['type']} new{iv['name'].capitalize()}, "

        iv2 = instanceVarList[-1]  # Last element
        constructorTemplate += f"{iv2['type']} new{iv2['name'].capitalize()}"
        constructorTemplate += ")\n\t{\n"

        for iv in instanceVarList:
            constructorTemplate += f"\t\t{iv['name']} = new{iv['name'].capitalize()};\n"

        constructorTemplate += "\t}\n"
        classFile.write(constructorTemplate)

        # Accessor Methods

        classFile.write("\n\t// Accessor Methods\n")
        accessorMethods = ""
        for iv in instanceVarList:
            accessorMethods += f"\tpublic {iv['type']} get{iv['name'].capitalize()}()\n\t{{\n\t\treturn {iv['name']};\n\t}}\n"

        accessorMethods += "\n"
        classFile.write(accessorMethods)

        if includeSetters:
            # Setter Methods
            classFile.write("\n\t// Setter Methods\n")
            setterMethods = ""
            for iv in instanceVarList:
                setterMethods += f"\tpublic void set{iv['name'].capitalize()}({iv['type']} new{iv['name'].capitalize()})\n\t{{\n\t\t{iv['name']} = new{iv['name'].capitalize()};\n\t}}\n"

            classFile.write(setterMethods)

        # End class
        classFile.write("}")


if __name__ == "__main__":
    main()
