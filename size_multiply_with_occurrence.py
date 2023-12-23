'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t, z):
    
    def unique_substrings(s):
        substrings = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substrings.add(s[i:j])
        return substrings

    substrings = unique_substrings(t)

    max_value = 0

    for substring in substrings:
        
        count = z.count(substring)

        product = len(substring) * count

        max_value = max(max_value, product)

    return max_value


if __name__ == '__main__':
    find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    
    result=find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print(result)
    

    