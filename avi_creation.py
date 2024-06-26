import struct
import urllib.request

# Create a minimal AVI file structure
avi_header = b'RIFF\x00\x00\x00\x00AVI LIST\x14\x01\x00\x00hdrlavih8\x00\x00\x00@\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xd0\x02\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00LISTt\x00\x00\x00strlstrh8\x00\x00\x00txts\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00strf(\x00\x00\x00(\x00\x00\x00\xd0\x02\x00\x00\xf0\x00\x00\x00\x01\x00\x18\x00XVID\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00LIST\x00\x00\x00\x00movi'

# Download function
def download_and_display():
    url = "https://binary.golf/5/5"
    with urllib.request.urlopen(url) as response:
        text = response.read().decode()
    return text

# Get the text
content = download_and_display()

# Create video frames with text
frames = b''
for char in content:
    frame = struct.pack('<4sI', b'00dc', 720*480*3) + (char.encode() * 720*480)
    frames += frame

# Finalize AVI structure
file_size = len(avi_header) + len(frames) + 4
avi_header = avi_header[:4] + struct.pack('<I', file_size - 8) + avi_header[8:]
movi_size = len(frames) + 4
avi_header = avi_header[:-4] + struct.pack('<I', movi_size) + avi_header[-4:]

# Write the file
with open('output.avi', 'wb') as f:
    f.write(avi_header)
    f.write(frames)
    f.write(b'idx1\x00\x00\x00\x00')

print("Created output.avi")