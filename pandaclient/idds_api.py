from . import Client


# API call class
class IddsApi(object):

    def __init__(self, name, dumper, verbose, idds_host, compress, manager):
        self.name = name
        if idds_host is not None:
            self.name += '+{}'.format(idds_host)
        self.dumper = dumper
        self.verbose = verbose
        self.compress = compress
        self.manager = manager

    def __call__(self, *args, **kwargs):
        return Client.call_idds_command(self.name, args, kwargs, self.dumper, self.verbose, self.compress,
                                        self.manager)


# interface to API
class IddsApiInteface(object):
    def __init__(self):
        self.dumper = None

    def __getattr__(self, item):
        return IddsApi(item, self.dumper, self.verbose, self.idds_host, self.compress, self.manager)

    def setup(self, dumper, verbose, idds_host, compress, manager):
        self.dumper = dumper
        self.verbose = verbose
        self.idds_host = idds_host
        self.compress = compress
        self.manager = manager


# entry for API
api = IddsApiInteface()
del IddsApiInteface


def get_api(dumper=None, verbose=False, idds_host=None, compress=True, manager=False):
    """Get an API object to access iDDS through PanDA

       args:
           dumper: function object to json-serialize data
           verbose: True to see verbose messages
           idds_host: iDDS hostname
           compress: True to compress request body
           manager: True to use ClientManager API
       return:
           an API object
    """
    api.setup(dumper, verbose, idds_host, compress, manager)
    return api
