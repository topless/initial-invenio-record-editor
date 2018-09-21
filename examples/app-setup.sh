#!/bin/sh

# quit on errors:
set -o errexit

# quit on unbound symbols:
set -o nounset

DIR=`dirname "$0"`

cd $DIR
export FLASK_APP=app.py

# Setup app
mkdir static
mkdir $DIR/instance

# npm install -g node-sass@3.8.0 clean-css@3.4.19 requirejs@2.2.0 uglify-js@2.7.3

flask npm
cd static
npm install
cd ..
flask collect -v
flask assets build

# FIXME: Copy static files
cp static/node_modules/test-invenio-record-editor-js/dist/fontawesome* static/gen
cp -r static/node_modules/test-invenio-record-editor-js/dist/assets static/
