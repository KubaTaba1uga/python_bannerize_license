import os
import argparse

# Banner to inject
BANNER = """/*
 * Copyright (c) 2025 Jakub Buczynski <KubaTaba1uga>
 * SPDX-License-Identifier: MIT
 * See LICENSE file in the project root for full license information.
 */
"""

# File extensions to process
EXTENSIONS = ['.c', '.h']

def inject_banner(file_path):
    with open(file_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        if content.lstrip().startswith('/*') and 'SPDX-License-Identifier' in content:
            print(f"[SKIP] {file_path} already has a banner.")
            return
        f.seek(0)
        f.write(BANNER + '\n' + content)
    print(f"[INJECTED] {file_path}")

def process_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in EXTENSIONS):
                inject_banner(os.path.join(dirpath, filename))

def main():
    parser = argparse.ArgumentParser(description="Inject a banner into C source and header files.")
    parser.add_argument('directory', type=str, help="Directory to process")
    args = parser.parse_args()

    if os.path.isdir(args.directory):
        process_directory(args.directory)
    else:
        print("Invalid directory.")

if __name__ == "__main__":
    main()
