"""
tested on Windows operator
"""
with open("header_converter_space", "r") as f:
    s = f.readlines()
o = []
for line in s:
    line_colon_sep = line.rstrip('\n').split(':')
    if len(line_colon_sep) == 2:
        key, val = line_colon_sep[0].strip(), line_colon_sep[1].strip()
    else:
        key, val = line_colon_sep[0].strip(), ':'.join(line_colon_sep[1:]).strip()
    o.append(f'"{key}": "{val}",\n')
with open("header_converter_space", "w") as f:
    f.writelines(o)
