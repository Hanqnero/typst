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

if __name__ == "__main__":
    notebook_path = 'python/notebook.ipynb'
    output_dir = 'python/cells'
    process_notebook(notebook_path, output_dir)