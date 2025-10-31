from file_searcher import find_file

def main():
    print("🔍 File Finder Tool")
    print("------------------")
    
    filename = input("Enter the file name you want to search: ").strip()
    
    # Optional: limit search to your user directory for faster search
    search_path = input("Enter the directory to search in (or press Enter for full system): ").strip()
    if search_path == "":
        search_path = "/"
    
    print("\nSearching... please wait.\n")
    results = find_file(filename, search_path)
    
    if results:
        print(f"✅ Found {len(results)} file(s):\n")
        for path in results:
            print("➡️", path)
    else:
        print("❌ File not found.")

if __name__ == "__main__":
    main()
