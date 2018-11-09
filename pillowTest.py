from PIL import Image

codeLib = "C8o.8Co"


def transport(image):
    codeImage = ''
    for i in range(0, image.size[1]):
        for j in range(0, image.size[0]):
            r, g, b = image.getpixel((j, i))
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            codeImage += codeLib[int(gray * len(codeLib) / 256)]
        codeImage += '\r\n'
    print(codeImage)
    with open('wang.txt', 'w') as f:
        f.write(codeImage)


if __name__ == '__main__':
    Im = Image.open('wang.jpg')
    Im.show()
    transport(Im)
