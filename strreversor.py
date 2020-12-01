"""
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
"""

s = input()
lower_list = ''
upper_list = ''
even_list = ''
odd_list = ''
for i in s:
    if i.islower():
        lower_list += i
    elif i.isupper():
        upper_list += i
    elif i.isdigit():
        if int(i) % 2 == 0:
            even_list += str(i)
        else:
            odd_list += str(i)

output = ''.join(sorted(lower_list))+ ''.join(sorted(upper_list))+ ''.join(sorted(odd_list))+ ''.join(sorted(even_list))
print(output)
        
