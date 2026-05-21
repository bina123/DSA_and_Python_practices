
def read_config(filename):
    config= {}
    try:
        with open(filename,'r') as file:
            for line in file:
                if not line or line.startswith("#"):
                    continue
                
                if "=" in line:
                    key, value = line.split("=")
                    config[key.strip()] = value.strip()
                    
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        
    return config
        
        

def write_config(output_file,config):
    with open(output_file,'w') as file:
        file.write("# Configuration file \n")
        file.write("# generated automatically \n\n")
        
        for key, val in config.items():
            file.write(f"{key}={val}\n")
            
def update_config(filename,key, value):
    config = read_config(filename)
    config[key] = value
    write_config(filename,config)

config = read_config('python-practice/config.txt')
print(config)

config['debug_mode'] = 'false'
config['new_setting'] = 'value'
write_config('python-practice/config_updated.txt', config)