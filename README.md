# kubernetes-python-stubs

Stub files for the [kubernetes python client](https://github.com/kubernetes-client/python), taken from [PyPI](https://pypi.org/project/kubernetes-stubs-elephant-fork/#history). Slight modifications were made:
 - Replaced all the detailed dictionary types with Any
 - Added the `_preload_content` argument to all the api functions
 - Replaced the return types to `BaseHTTPResponse` to because I have `_preload_content=False` everywhere

## Usage

`git submodule add https://github.com/Bladieblah/kubernetes-python-stubs.git typings/kubernetes`
