# Notebook Processor

This project provides a Python script to process Jupyter notebooks. It reads a specified notebook file, separates it into individual cells, and saves each cell into a numbered file for easier management and access.

## Features

- Reads Jupyter notebook files in `.ipynb` format.
- Separates the notebook into individual cells.
- Saves each cell as a separate file with a numbered naming convention.

## Requirements

To run this project, you need to install the following dependencies:

- `nbformat`: A library for reading and writing Jupyter notebook files.

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the source code.
2. Install the required dependencies.
3. Run the script located in `src/process_notebook.py` with the path to your notebook file as an argument.

Example command:

```
python src/process_notebook.py path/to/your/notebook.ipynb
```

This will create numbered files for each cell in the specified notebook.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.