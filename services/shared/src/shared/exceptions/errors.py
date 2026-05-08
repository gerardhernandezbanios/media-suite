class DbServiceError(Exception):
    pass

class NotFoundError(DbServiceError):
    pass

class ConflictError(DbServiceError):
    pass
