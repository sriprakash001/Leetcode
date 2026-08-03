class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace(".","[.]")
        # ans = []
        # for i in range(len(address)):
        #     if address[i] == ".":
        #         ans.append("[.]")
        #     else:
        #         ans.append(address[i])
        # return "".join(ans)
        x = [ "[.]" if address[i] == "." else address[i] for i in range(len(address))   ]
        return "".join(x)