import url_extractor


def main():
    extractor = url_extractor.url_extractor("https://bytebank.com/cambio?moeda=Real&valor=5")
    print(extractor)

if __name__ == '__main__':
    main()

