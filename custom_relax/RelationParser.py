import re

class Parser:
    def __init__(self):
        self.relations = {}

    def parse_relation(self, relation_text):
        match = re.match(r'(\w+)\s*\((.*?)\)\s*=\s*{\s*(.*?)\s*}', relation_text)
        # \w+ groups the relation name, \s* = whitespace, \( = respective brackets, *? embedded = any parameter, \s*=\s.. is "=" padded potentially space padded, then a padded (.*?) for data entries
        # this is all compared againt the entered text "relation_text"
        if match:
            relation_name = match.group(1) # aka \w+
            attributes = [attr.strip() for attr in match.group(2).split(',')] # aka first (.*?)

            data_entries = match.group(3).split() # aka second (.*?)
            num_attributes = len(attributes)

            # Split data_entries into chunks of size num_attributes
            data = []

            for i in range(0, len(data_entries), num_attributes): 
                chunk = data_entries[i:i + num_attributes]
                print(chunk)
                data.append(chunk)
    
             # Convert data to tuples by iterating on chunks and stripping white spaces then using those strings for tuple data
            data = [tuple(entry.strip() for entry in entry_tuple) for entry_tuple in data]
    
            # Create the relation dictionary
            relation_dict = {"attributes": attributes, "data": data}
    
            # Store the relation dictionary
            self.relations[relation_name] = relation_dict

            print(self.relations)
            self.relations[relation_name] = {"attributes": attributes, "data": data}
            print(relation_name)
            print(attributes)
            print(data)
        else:
            raise ValueError("failed relation parse: invalid format")

    def execute_query(operation, condition, relation_name):
        if relation_name in self.relations:
            if operation == "select":
                pass
            elif operation == "project":
                pass
        else:
            raise ValueError("Unsupported operation or relation does not exist")
        
    def parse_query(self, query_text):
        match = re.match(r'(\w+)\s+(.*?)\((.*?)\)', query_text)
        # matches for \w+(operation) then .*?(condition) and .*?(relation_name)
        if match:
            operation = match.group(1)
            condition = match.group(2)
            relation_name = match.group(3)

            print(operation)
            print(condition)
            print(relation_name)
            return operation, condition, relation_name;
        else:
            raise ValueError("Invalid query format")

    def run(self):
        while True:
            user_input = input("Enter a relation or query (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                break

            try:
                if "select" in user_input:
                    operation, relation_name = self.parse_query(user_input)
                    self.execute_query(operation, relation_name)
                else:
                    self.parse_relation(user_input)
                    print("Relation successfully parsed.")

            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    parser = Parser()
    parser.run()
