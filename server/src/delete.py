#!/usr/bin/env python
# -*- Mode: Python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# vim:set ft=python ts=4 sw=4 sts=4 autoindent:

'''
Deletion functionality.
'''

from __future__ import with_statement

from os.path import join as path_join
from message import Messager
from config import DATA_DIR

import shutil

def delete_document(collection, document):
    fullPath = path_join(DATA_DIR, collection[1:], document)
    trashPath = path_join(DATA_DIR, "trash")
    Messager.info("Moving file and annotations from {} to {}".format(fullPath, trashPath))
    shutil.move("{}.txt".format(fullPath), trashPath)
    shutil.move("{}.ann".format(fullPath), trashPath)
    #Messager.error("Document deletion not supported in this version.")
    return {}

def delete_collection(collection):
    Messager.error("Collection deletion not supported in this version.")
    return {}
     
