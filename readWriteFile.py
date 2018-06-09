# will overwrite

"""
# Copy file
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
"""

crop = 0
with open('keyart1_fade.jpg', 'rb') as rf:
    with open('test_copy.jpg', 'wb') as wf:
        for line in rf:
            crop = crop +1
            # write file to wf but stop after crop specified
            if crop < 256:
                wf.write(line)

# Copy Picture in chunks
"""
with open('keyart1_fade.jpg', 'rb') as rf:
    with open('test_copy.jpg', 'wb') as wf:

        chunk_size = 4096

        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
"""

"""
        for line in rf:
            wf.write(line)
"""
