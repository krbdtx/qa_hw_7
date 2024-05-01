import os
import shutil
import pytest
from zipfile import ZipFile

parent_dir = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(parent_dir, 'tmp')
source_dir = os.path.join(parent_dir, 'resources')


@pytest.fixture(scope='session', autouse=True)
def archive():
    if not os.path.exists(source_dir):
        os.mkdir(source_dir)
    with ZipFile(os.path.join(source_dir, 'zip_file.zip'), 'w') as archive:
        for filename in os.listdir(path):
            archive.write(os.path.join(path, filename), arcname=filename)
    yield
    shutil.rmtree(source_dir)
