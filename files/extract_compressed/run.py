import os
import tarfile, zipfile

zip_source = 'data/zip/train_z.zip'
tar_source = 'data/tar/train_t.tar'
destination = 'data/output/'


def custom_extract_tar(source_file_path, destination_path):
    tar = tarfile.open(source_file_path)
    tar.extractall(destination_path)
    tar.close()


def custom_extract_zip(source_file_path, destination_path):
    zip_ref = zipfile.ZipFile(source_file_path, 'r')
    zip_ref.extractall(destination_path)
    zip_ref.close()

# extract
custom_extract_zip(zip_source, destination)
custom_extract_tar(tar_source, destination)