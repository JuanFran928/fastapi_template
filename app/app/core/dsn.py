from pydantic import AnyUrl


class MysqlDsn(AnyUrl):
    allowed_schemes = {
        'mysql',
        'mysql+pymysql'
    }
    user_required = True
