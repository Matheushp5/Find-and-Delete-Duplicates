import csv, hashlib

def find_delete_duplicates(file_path):
    data = []
    duplicates = set()
    #open and read the csv file
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                #hash the row
                hash_object = hashlib.md5(str(row).encode())
                hex_dig = hash_object.hexdigest()
                #check if the row is duplicate
                if hex_dig not in duplicates:
                    duplicates.add(hex_dig)
                    data.append(row)
                else:
                    print(f"Duplicate Entry : {row}")
    #prompt the user if they want to delete duplicate
    response = input("Deletar itens duplicados? (s/n)")
    #if yes, write the new file without duplicates
    if response.lower() == "s":
        with open(file_path, "w", newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
        removed = True
        
    if removed:
        print("Removido!")

# call the function 
find_delete_duplicates("file.csv")
