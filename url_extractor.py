import re

class url_extractor:
    def __init__ (self, url):
        self.url = self.sanitize_url(url)
        self.url_validation(url)

    def sanitize_url (self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def url_validation (self, url):
        if url == "":
            raise ValueError("A URL está vazia")
        else:
            url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio?')
            match = url_pattern.match(url)
            if not match:
                raise ValueError("A URL não é válida")

    def get_base_url (self):
        index = self.url.find('?')
        base_url = self.url[:index]
        return base_url

    def get_params (self):
        index = self.url.find('?')
        params = self.url[index+1:]
        return params

    def get_param_value (self, param):
        index_param = self.url.find(param)
        index_value = index_param + len(param) + 1
        index_commercial_e = self.url.find('&', index_value)
        if index_commercial_e != -1:
            return self.url[index_value:]
        else:
            return self.url[index_value:index_commercial_e]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_params() + "\n" + "URL Base: " + self.get_base_url()

    def __eq__(self, other):
        self.url == other.url