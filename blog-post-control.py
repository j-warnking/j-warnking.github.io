#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:07:56 2023

@author: jacopowarnking
"""
import os 
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

from git import Repo
from pathlib import Path

PATH_TO_BLOG_REPO = Path('/Users/jacopowarnking/GitHub/j-warnking.github.io/.git')

PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent

PATH_TO_CONTENT = PATH_TO_BLOG/"content"

def update_blog(commit_message='Updates blog'): 
    # GitPython -- Repo Location
    repo = Repo(PATH_TO_BLOG_REPO)
    
    # git add
    repo.git.add(all=True)
    
    # git commit -m "updates blog"
    repo.index.commit(commit_message)
    
    # git push
    origin = repo.remote(name='origin')
    origin.push()
    

random_text = "asdf;afsljfl;asjfl;aj"

with open(PATH_TO_BLOG/"index.html", 'w') as f:
    f.write(random_text)
    

