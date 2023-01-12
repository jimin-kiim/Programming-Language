import global_variables as g
class ActivationRecord:
    def __init__(self, name):
        self.name = name
        self.local_variables = []
        self.dynamic_link = 0
        self.return_address = {}
        self.callees = []
        # self.is_called = False
        self.is_there_print_ari = False

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        return self.members[key]

    def get(self, key):
        return self.members.get(key)

    def set_is_called_true(self):
        # self.is_called = True
        for callee in self.callees:
            # print(callee)
            for ari in g.aris:
                if ari.name == callee:
                    g.run_time_stack.append(ari)
                    # ari.set_is_there_print_ari_true()
                    ari.set_is_called_true()
        print(self.is_there_print_ari)
        if self.is_there_print_ari:
            for ari in g.run_time_stack: 
                print()
                print(ari.name+":",end="")
                for var in ari.local_variables:
                    print("Local variable:",var)
                print("Dynamic Link:",ari.dynamic_link)
                print("Return Address:",ari.return_address)
                print()

    def set_is_there_print_ari_true(self):
        self.is_there_print_ari = True