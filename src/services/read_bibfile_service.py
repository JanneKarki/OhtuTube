
class ReadBibfileService:

    def decode_bibfile(self, bibfile):
        data = bibfile.split("@")
        data.pop(0)
        references = []
        for reference in data:
            content = reference.split("\n")
            ref_id = self.read_id(content[0])
            author = self.read_str_input(content[1])
            title = self.read_str_input(content[2])
            year = self.read_int_input(content[3])
            publisher = self.read_str_input(content[4])
            address = self.read_str_input(content[5])
            references.append((ref_id, author, title, year, publisher, address))
        return references

        
    def read_id(self, string):
        reference_id = ""
        for index, char in enumerate(string):
            if char == "{":
                for id_char in range(index, len(string)-2):
                    index += 1
                    if id_char == " ":
                        break
                    reference_id += string[index]
        return reference_id

    def read_str_input(self, string):
        string_input = ""
        for index, char in enumerate(string):
            if char == "{":
                start = index
            if char == "}":
                end = index
                string_input += string[start+1:end]
                break
                    
        return string_input[1:-1]

    def read_int_input(self, integer):
        integer_input = ""
        for index, char in enumerate(integer):
            if char == "{":
                index += 1
                for id_char in range(index+1, len(integer)-3):
                    index +=1
                    if id_char == "}":
                        break
                    integer_input += integer[index]
        return integer_input
