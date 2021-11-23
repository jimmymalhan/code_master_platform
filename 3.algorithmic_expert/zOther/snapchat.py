class BraceExpansion:
    def __init__(self, input_string):
        self.input_string = input_string
        self.output_string = []

    def expand_braces(self):
        start = self.input_string.index("{")+1
        end = self.input_string.index("}")
        for num in self.input_string[start:end].split(","):
            self.output_string.append(f"{self.input_string[:start-1]}{num}{self.input_string[end+1:]}")

        return self.output_string

    def check_for_empty_list(self):
        if self.output_string == []:
            return False
        else:
            return True

def main():
    input_string = "file{0,1}.txt"
    brace_expansion = BraceExpansion(input_string)
    output_string = brace_expansion.expand_braces()
    print(output_string)

    if brace_expansion.check_for_empty_list():
        print("List is not empty")
    else:
        print("List is empty")

if __name__ == '__main__':
    main()