def encode(arr):
    final = ""
    for item in arr:
        final += (item+str(len(item)))
    return final
    
def decode(arr):
    tempStr = ""
    final = []
    for item in list(arr):
        if not item.isdigit():
            tempStr += item
        else:
            final.append(tempStr)
            tempStr = ""

    return final
    
    

print(decode(encode(["neet","code","love","you"])))
print(decode(encode(["we","say",":","yes"])))
    
    
# By GPT
# def encode(arr):
#     final = ""
#     for item in arr:
#         final += item + str(len(item)) + " "  # Add a separator space after each encoded string
#     return final.strip()  # Remove the trailing space


# def decode(arr):
#     final = []
#     i = 0
#     while i < len(arr):
#         j = i
#         # Move j until we find a digit, which represents the length of the string
#         while j < len(arr) and not arr[j].isdigit():
#             j += 1
        
#         length_str = ""
#         # Collect the digits (length of the string)
#         while j < len(arr) and arr[j].isdigit():
#             length_str += arr[j]
#             j += 1
        
#         # Extract the original string using the length
#         length = int(length_str)
#         final.append(arr[i:i+length])
        
#         # Move the pointer i to the next encoded string
#         i = j + 1

#     return final


# # Test cases
# print(decode(encode(["neet", "code", "love", "you"])))
# print(decode(encode(["we", "say", ":", "yes"])))
