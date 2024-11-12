import os
import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor


project_root = os.getcwd()
inputs_list = [
    [os.path.join(project_root, 'notebooks'), 'custom-roi-tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks'), 'roi-circle-tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks'), 'roi-rectangle-tutorial.ipynb']
]

@pytest.mark.parametrize('dir,notebook', inputs_list)
def test_notebook(dir, notebook, tmpdir):
    """Test the notebook."""
    tmp = tmpdir.mkdir('sub')
    # Open the notebook
    with open("index.ipynb", "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)
