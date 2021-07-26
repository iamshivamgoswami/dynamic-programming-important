class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans=0
        heads=[[]for i in range(26)]
        for word in words:
            it=iter(word)
            heads[ord(next(it))-ord("a")].append(it)
        for letters in s:
            letter_index=ord(letters)-ord("a")
            old_bucket=heads[letter_index]
            heads[letter_index]=[]
            while old_bucket:
                it=old_bucket.pop()
                nxt=next(it,None)
                if nxt:
                    heads[ord(nxt)-ord("a")].append(it)
                else:
                    ans+=1
        return ans