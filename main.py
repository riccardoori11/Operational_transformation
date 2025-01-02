class Document:

    def __init__(self, document):
        self.document = document
    
    def operation(self, operation):
        """Apply an operation to the document."""
        if operation["type"] == "insert":
            pos = operation["pos"]
            char = operation["char"]
            self.document = self.document[:pos] + char + self.document[pos:]
        elif operation["type"] == "delete":
            pos = operation["pos"]
            length = operation["length"]
            self.document = self.document[:pos] + self.document[pos + length:]


class OT:

    def insert_insert(self,op1,op2):

        if op1['pos'] < op2['pos']:
            return op1
        else:
            op1["pos"] += len(op2["char"])
            return op1

    def insert_delete(self,op1,op2):
        if op1['pos'] < op2['pos']:
            return op1
        elif op1["pos"] >= op2["pos"] + op2["length"]:
                op1["pos"] -= op2["length"]
                return op1
    
    def delete_insert(self,op1,op2):
        if op1['pos'] < op2['pos']:
            return op1
        elif op1['pos'] >= op2['pos']:
            op1['pos'] += len(op2['char'])
            return op1
        # This happens when you want to insert a character that was in the interval of the deleting operation
        else:
            segment1 = {"type": "delete", "pos": op1['pos'], "length": op2['pos'] - op1['pos']}
            segment2 = {
                "type": "delete",
                "pos": op2['pos'] + len(op2['char']),
                "length": op1['length'] - (op2['pos'] - op1['pos']),
            }
            return segment1, segment2
        
    def delete_delete(self, op1, op2):
        if op2['pos'] >= op1['pos'] + op1['length']:

            return op1
        elif op2['pos'] + op2['length'] <= op1['pos']:

            op1['pos'] -= op2['length']
            return op1
        elif op2['pos'] <= op1['pos'] and op2['pos'] + op2['length'] >= op1['pos'] + op1['length']:

            op1['length'] = 0
            return op1
        elif op2['pos'] <= op1['pos']:

            op1['length'] -= (op2['pos'] + op2['length']) - op1['pos']
            op1['pos'] = op2['pos']
            return op1
        else:

            op1['length'] = op2['pos'] - op1['pos']
            return op1

document = Document("123456")
document.operation({"type": "insert", "pos": 3, "char": "a"})
#print(document.document)  123a456


ot = OT()
op1 = {"type": "insert", "pos": 3, "char": "a"}
op2 = {"type": "insert", "pos": 2, "char": 'b'}
new_insert_of_op1_and_op2 = ot.insert_insert(op1,op2)
print(new_insert_of_op1_and_op2)
        
