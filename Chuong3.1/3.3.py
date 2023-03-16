alp=str(input())
if len(alp)>1:
    print('Khong hop le')
elif alp=='a' or alp=='e' or alp=='o' or alp=='i' or alp=='u':
    print('The letter is vowel')
elif alp=='y':
    print('The letter is vowel or is consonant')
else:
    print('The letter is a consonant')