class Solution:

    def encode(self, strs: List[str]) -> str:
        tmp = ""
        for i in strs:
            tmp+= str(len(i)) + "#" + i

        return tmp

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        answer = []
        while j <(len(s)):
            if s[j]=="#":
                length = int(s[i:j])
                word = s[j+1:j+1+length]
                answer.append(word)
                i = j+length+1
                j = i
            
            else:
                j+=1


        return answer