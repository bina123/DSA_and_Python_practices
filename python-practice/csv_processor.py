def read_csv(filename):
    data = []
    
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            
            if not lines:
                return data
            
            headers = lines[0].strip().split(",")
            
            for line in lines[1:]:
                values = line.strip().split(",")
                row = dict(zip(headers,values))
                data.append(row)
                
    except FileNotFoundError:
        print(f"Error : {filename} not found")
        return []
    
    return data    

def write_csv(filename, data, headers):
    with open(filename,'w') as file:
        file.write(','.join(headers) + "\n")
        
        for row in data:
            values = [str(row.get(h,'')) for h in headers]
            file.write(','.join(values) + "\n")
                
def filter_csv(inputfile,outfile,condition):
    data = read_csv(inputfile)
    filtered = [row for row in data if condition(row)]
    
    if data:
        headers = list(data[0].keys())
        write_csv(outfile,filtered,headers)
        
    return filtered

students = read_csv('python-practice/students.csv')
print(students)

# Filter students with grade A
a_students = filter_csv(
    'python-practice/students.csv',
    'python-practice/a_students.csv',
    lambda row: row.get('grade') == 'A'
)
print(f"Found {len(a_students)} A students")