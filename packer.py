import os
import argparse
import pathspec

def load_gitignore(root_path):
    gitignore_path = os.path.join(root_path, '.gitignore')
    if not os.path.exists(gitignore_path):
        return None
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        return pathspec.PathSpec.from_lines('gitwildmatch', f)

def is_text_file(filepath):
    try:
        with open(filepath, 'tr', encoding='utf-8') as check_file:
            check_file.read(1024)
            return True
    except UnicodeDecodeError:
        return False
    except Exception:
        return False

def pack_repo(target_dir, output_file):
    spec = load_gitignore(target_dir)
    default_ignores = ['.git', '__pycache__', '.venv', 'node_modules', 'venv']
    
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(f"# Repository Context: {os.path.basename(os.path.abspath(target_dir))}\n\n")
        
        for root, dirs, files in os.walk(target_dir):
            dirs[:] = [d for d in dirs if d not in default_ignores]
            
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, target_dir)
                
                if spec and spec.match_file(rel_path):
                    continue
                
                if not is_text_file(file_path):
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    out.write(f"## File: `{rel_path}`\n")
                    out.write("```\n")
                    out.write(content)
                    out.write("\n```\n\n")
                except Exception as e:
                    print(f"Skipping {rel_path}: {e}")

    print(f"Context successfully packed into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pack repository into a single markdown file for LLM context.")
    parser.add_argument("directory", nargs="?", default=".", help="Target directory (default: current)")
    parser.add_argument("-o", "--output", default="context_output.md", help="Output file name")
    
    args = parser.parse_args()
    pack_repo(args.directory, args.output)