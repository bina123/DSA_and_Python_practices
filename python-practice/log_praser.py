def parse_log_file(filename):
    errors = []
    
    try:
        with open(filename,'r') as file:
            for line_num, line in enumerate(file,1):
                if "[ERROR]" in line:
                    errors.append({
                        "line": line_num,
                        "message" : line.strip()
                    })
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return [] 
    
    return errors

def write_error_report(errors, output_file):
    with open(output_file,'w') as file:
        file.write("Error Report\n")
        file.write("="*50 + "\n\n")
        
        if not errors:
            file.write("No errors found")
        else:
            for error in errors:
                file.write(f"Line: {error['line']}: {error['message']}\n")


errors = parse_log_file('python-practice/log.txt')
print(f"Found {len(errors)} errors")
write_error_report(errors, 'python-practice/error_report.txt')