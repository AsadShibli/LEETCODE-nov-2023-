class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowel_index = []
        vowel_list  =[]
        consonent_index = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_index.append(i)
                vowel_list.append(s[i])
            else:
                consonent_index.append(i)
        vowel_list.sort()
        result = list(s)
        for i ,v_index in enumerate(vowel_index):
            result[v_index] = vowel_list[i]
        return "".join(result)
