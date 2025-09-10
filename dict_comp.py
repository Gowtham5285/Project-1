result = ""

def allVowels(ch):
    global result      
    result += ch       
    return result      

a = {"name1": "vamsi", "name2": "ravi"}

res = {allVowels(j) for i in a for j in a[i] if j in "aeiouAEIOU"}

print(result)
