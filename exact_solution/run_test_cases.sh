#!/bin/bash
# predefined file paths
exact_path=./
approx_path=../approximate_solution/
if [ $# -lt 1 ]; then
    ver="exact"
else
    ver=$1
fi
if [ $ver == "exact" ] || [ $ver == "e" ]; then
    test_path="${exact_path}test_cases/"
    type="exact"
    executable_path=$exact_path
elif [ $ver == "approx" ] || [ $ver == "a" ]; then
    test_path="${approx_path}test_cases/"
    type="approx"
    executable_path=$approx_path
else
    echo "Bad value passed: ${ver}"
    echo "Expects either no arg, \"exact\", \"e\", \"approx\", or \"a\"."
    exit
fi
# iterate over the intended tests
for file in "${test_path}inputs/"*.txt; do
    # extract the file name (with extension) from the path
    base_name=$(basename ${file})
    if [ -e "$file" ] && [ -f "$file" ] && [ -s "$file" ]; then
        sed "s/\r//" "$file" | python3 "${executable_path}cs412_minvertexcover_${type}.py" > "${test_path}outputs/out_${base_name}"
    fi
done
