# kubernetes-python-stubs

Stub files for the kubernetes python client, taken from https://pypi.org/project/kubernetes-stubs-elephant-fork/#history. Slight modifications were made:
 - Replaced all the detailed dictionary types with Any
 - Added the `_preload_content` argument to all the api functions
 - Replaced the return types to `BaseHttpResponse` to because I have `_preload_content=False` everywhere
