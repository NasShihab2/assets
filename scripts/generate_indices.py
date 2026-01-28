import json
import os
import re


def scan_assets():
    """Scans directories and returns a list of asset dictionaries."""
    configs = [
        {"dir": "svg", "type": "svg", "ext": [".svg"]},
        {"dir": "lottie", "type": "lottie", "ext": [".json"]},
        {"dir": "images", "type": "image", "ext": [".png", ".jpg", ".jpeg"]},
        {"dir": "gif", "type": "image", "ext": [".gif", ".jpg"]},
        {"dir": "document", "type": "doc", "ext": [".md", ".html"]},
        {"dir": "dart", "type": "dart", "ext": [".dart", ".md", ".txt"]},
        {"dir": "fonts", "type": "font", "ext": [".ttf", ".otf", ".woff", ".woff2"]}
    ]
    
    all_assets = []
    
    for config in configs:
        if os.path.exists(config["dir"]):
            # Filter files by extension
            files = sorted([f for f in os.listdir(config["dir"]) if any(f.endswith(ext) for ext in config["ext"])])
            for f in files:
                all_assets.append({
                    "name": f,
                    "type": config["type"],
                    "path": f"{config['dir']}/{f}"
                })
    
    return all_assets

def update_index_html(assets):
    """Updates the assets array in index.html using markers."""
    index_path = "index.html"
    if not os.path.exists(index_path):
        print(f"Error: {index_path} not found.")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Generate the JS array string
    assets_js = "    const assets = " + json.dumps(assets, indent=2) + ";"
    
    # Replace the content between markers
    marker_start = "/* @assets-start */"
    marker_end = "/* @assets-end */"
    
    pattern = re.escape(marker_start) + r".*?" + re.escape(marker_end)
    new_content = re.sub(pattern, f"{marker_start}\n{assets_js}\n    {marker_end}", content, flags=re.DOTALL)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Successfully updated {index_path} with {len(assets)} assets.")

if __name__ == "__main__":
    print("Scanning for assets...")
    assets = scan_assets()
    update_index_html(assets)
