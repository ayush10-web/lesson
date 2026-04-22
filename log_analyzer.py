def analyze_logs(file_path):
    counts = {
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }

    total = 0

    try:
        with open(file_path,"r") as file:
            for line in file:
                total +=1


                if "INFO" in line:
                    counts["INFO"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "FAILED" in line:
                    counts["ERROR"] += 1
        
        return counts,total
    
    except FileNotFoundError:
        print("file not found.")
        return None,0
    
def main():
    result,total = analyze_logs("logs.txt")

    if result:
        print("===log summary ====")
        print(f"total logs:{total}")


        for key,value in result.items():
            print(f"{key}:{value}")


if __name__ == "__main__":
    main()        

