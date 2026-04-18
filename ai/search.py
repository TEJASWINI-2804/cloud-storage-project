from database import files_collection

def search_files(query):
    results = list(files_collection.find({}))

    filtered = []
    for item in results:
        if query.lower() in item["filename"].lower() or \
           any(query.lower() in tag.lower() for tag in item.get("tags", [])):
            filtered.append({
                "filename": item["filename"],
                "tags": item.get("tags", [])
            })

    # Remove duplicates
    unique_results = []
    seen = set()

    for item in filtered:
        if item["filename"] not in seen:
            unique_results.append(item)
            seen.add(item["filename"])

    return unique_results