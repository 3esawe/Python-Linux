def insert_star_between_pairs(a_string):
    if a_string is None:
        return None
    elif len(a_string) <= 1:
        return a_string
    elif a_string[0:1] == a_string[1:2]:
        return a_string[0:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)])

    return a_string[0:1] + insert_star_between_pairs(a_string[1:len(a_string)])
print(insert_star_between_pairs("ccc"))


pre_ordered_list = []
class BinaryTree:
    
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder(self):
        pre_ordered_list.append(self.get_root_val())
        if self.get_left_child():
            self.get_left_child().preorder()
        if self.get_right_child():
            self.get_right_child().preorder()  
     


    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data