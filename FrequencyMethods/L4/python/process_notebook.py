#!/usr/bin/env python3
import nbformat
import os

def process_notebook(notebook_path, output_dir):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, cell in enumerate(c for c in notebook_content.cells if c.cell_type == 'code'):
        if cell.cell_type == 'code':
            cell_filename = os.path.join(output_dir, f'cell_{i + 1}.py')
            with open(cell_filename, 'w', encoding='utf-8') as cell_file:
                source = cell.get('source', '')
                cell_file.write(source)

    total_files = len([cell for cell in notebook_content.cells if cell.cell_type == 'code'])
    last_cell_path = os.path.join(output_dir, 'last_cell.txt')
    with open(last_cell_path, 'w', encoding='utf-8') as last_file:
        last_file.write(str(total_files))

if __name__ == "__main__":
    from sys import argv

    # check if 2 arguments are passed
    if len(argv) < 3:
        print("Usage: python process_notebook.py notebook_path")
        exit(1)

    notebook_path = argv[1]
    output_dir = argv[2]
    process_notebook(notebook_path, output_dir)