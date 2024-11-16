# Set the PYTHONPATH to include both the src directory and the parent directory
export PYTHONPATH=$(pwd):$(pwd)/src:$PYTHONPATH
echo "PYTHONPATH set to $(pwd) and $(pwd)/src"
