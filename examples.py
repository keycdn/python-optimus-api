import optimus


def main():
    # create an Optimus API Client and pass licence key
    api = optimus.Api('<your_license_key>')

    # now open your ouput file as binary for writing
    with open('output.jpg', 'wb') as output:
        # call the optimize method
        result = api.optimize('image.jpg')
        # and write the result to output
        output.write(result)

    # Convert to WebP image format
    with open('output.webp', 'wb') as output:
        result = api.optimize('image.jpg', 'webp')
        output.write(result)

    # Compress and optimize your image, but keep the metadata
    with open('output.jpg', 'wb') as output:
        result = api.optimize('image.jpg', 'clean')
        output.write(result)

if __name__ == '__main__':
    main()
