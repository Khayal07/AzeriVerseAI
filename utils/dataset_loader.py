def load_dataset(file_path):
    
    with open(file_path, "r", encoding="utf-8") as file:
        
        data = file.read()
        
    return data