#!/bin/bash

git fast-export 'HEAD' | ./dulwich_bug.py
