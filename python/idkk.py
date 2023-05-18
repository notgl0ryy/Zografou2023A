number=input("Give number: ")
transform={'0':'zero',
           '1':'one',
           '2':'two',
           '3':'three',
           '4':'four',
           '5':'five',
           '6':'five',
           '7':'six',
           '8':'eight',
           '9':'nine'}
output=" "

for number in number:
    output+=transform[number]+' '

print(output)