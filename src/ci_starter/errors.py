class CiStarterError(Exception):
    pass


class RemoteNotFoundError(CiStarterError):
    code = 3

    def __str__(self):
        return "could not find any remote in the repository"
