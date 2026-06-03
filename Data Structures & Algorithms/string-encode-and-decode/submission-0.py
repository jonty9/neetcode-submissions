class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for i in strs:
            encoding+=str(len(i))
            encoding+="#"            
            for j in i:
                encoding+=j
        return encoding

    def decode(self, s: str) -> List[str]:
        decoded = []
        string = ""
        i = 0
        while i != len(s):
                stringLength = ""
                while s[i] != "#":
                    print(s[i])
                    stringLength+=s[i]
                    i+=1
                print(repr(stringLength))
                stringLength = int(stringLength.strip())

                char = ""
                for k in range(stringLength):
                    i+=1
                    char += s[i]
                decoded.append(char)
                i+=1
        return decoded
