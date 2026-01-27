import os


def generate_markdown(directory, title, file_extensions, has_preview=True):
    files = sorted([f for f in os.listdir(directory) if any(f.endswith(ext) for ext in file_extensions)])
    if not files:
        return

    md_content = f"# {title}\n\nThis folder contains {title.lower()}.\n\n### 📦 Files\n\n"
    
    if has_preview:
        md_content += "| Preview | Name | Link |\n| :---: | :--- | :--- |\n"
        for f in files:
            md_content += f"| <img src=\"{f}\" width=\"40\"> | {f} | [View]({f}) |\n"
    else:
        md_content += "| File Name | Link |\n| :--- | :--- |\n"
        for f in files:
            md_content += f"| **{f}** | [Download]({f}) |\n"

    md_content += "\n[Back up to Repository Root](../README.md)\n"
    
    with open(os.path.join(directory, f"{directory}.md"), "w", encoding="utf-8") as f:
        f.write(md_content)

if __name__ == "__main__":
    # Configure directories and their properties
    configs = [
        {"dir": "lottie", "title": "Lottie Animations", "ext": [".json"], "preview": False},
        {"dir": "svg", "title": "SVG Icons", "ext": [".svg"], "preview": True},
        {"dir": "images", "title": "Images", "ext": [".png", ".jpg", ".jpeg"], "preview": True},
        {"dir": "gif", "title": "GIFs", "ext": [".gif"], "preview": True}
    ]

    for config in configs:
        if os.path.exists(config["dir"]):
            generate_markdown(config["dir"], config["title"], config["ext"], config["preview"])
            print(f"Generated {config['dir']}/{config['dir']}.md")
