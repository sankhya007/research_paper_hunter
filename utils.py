import os
import shutil
import requests

def download_pdf(url, filename):

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            return filename
        else:
            print("❌ Failed to download PDF")
            return None

    except Exception as e:
        print("Download error:", e)
        return None

def list_downloaded_papers():

    import os

    if not os.path.exists("output"):
        print("No downloaded papers yet.")
        return []

    folders = os.listdir("output")

    print("\n📂 Downloaded Papers:\n")

    for i, f in enumerate(folders):
        print(f"[{i}] {f}")

    return folders

def save_extracted_insights(output_folder, insights, formulas, implementations):

    import os

    # Ensure folder exists (double safety)
    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, "important.txt")

    try:
        with open(file_path, "w", encoding="utf-8") as f:

            f.write("=== IMPORTANT INSIGHTS ===\n\n")
            for i in insights:
                f.write(f"- {i}\n")

            f.write("\n=== FORMULAS ===\n\n")
            for form in formulas:
                f.write(f"- {form}\n")

            f.write("\n=== IMPLEMENTATION IDEAS ===\n\n")
            for imp in implementations:
                f.write(f"- Idea: {imp['idea']}\n")
                f.write(f"  Code: {imp['pseudo_code']}\n")
                f.write(f"  Difficulty: {imp['difficulty']}\n\n")

    except Exception as e:
        print("❌ Failed to write file:", e)