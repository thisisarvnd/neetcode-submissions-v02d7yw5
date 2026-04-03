class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            length = len(i)
            result = result + str(length) + "x" + i
        return result

    def decode(self, s: str) -> List[str]:
        words = []
        current_index = 0
        num = ""
        while current_index != len(s):
            if s[current_index] == "x":
                word = ""
                length = int(num)
                current_index += 1 # to skip "5x" and start with the actual word
                for j in range(current_index,current_index + length):
                    word = word + s[j]
                words.append(word)
                current_index+=length
                num = ""


            else:
                num = num + s[current_index]
                current_index+=1
        return words

