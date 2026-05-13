def check_file_extention(filename):
    filename = filename.lower().strip()
    
    if filename.endswith('.jpg') or filename.endswith('jpeg'):
        return "Image file (jpeg)"
    elif filename.endswith(".png"):
        return "Image file (PNG)"
    elif filename.endswith(".pdf"):
        return "PDF Document"
    else:
        return "Unknown file type"

file = input("Enter filename: ")
result = check_file_extention(file)
print(result)