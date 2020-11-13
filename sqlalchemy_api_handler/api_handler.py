from pprint import pprint
from sqlalchemy import BigInteger,\
                       Column
from sqlalchemy.orm import synonym

from sqlalchemy_api_handler.bases.activator import Activator
from sqlalchemy_api_handler.utils.humanize import humanize


class ApiHandler(Activator):

    id = Column(BigInteger,
                primary_key=True,
                autoincrement=True)

    dehumanizedId = synonym('id')

    @property
    def humanizedId(self):
        return humanize(self.id)

    def dump(self):
        pprint(vars(self))

    def __repr__(self):
        self_id = "unsaved"\
               if self.id is None\
               else str(self.id) + "/" + humanize(self.id)
        return '<%s #%s>' % (self.__class__.__name__, self_id)
