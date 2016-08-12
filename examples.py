import optimus-api


def main():
    # create an Optimus API Client and pass licence key
    api = optimus.api.Client('<your_license_key>')

    # now open your ouput file as binary for writing
    with open('output.jpg', 'wb') as output:
        # call the optimize method
        result = api.optimize('image.jpg')
        # and write the result to output
        output.write(result)

if __name__ == '__main__':
    main()
