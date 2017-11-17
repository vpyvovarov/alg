import pytest
from union_find.quick_find import QuickFind
from union_find.quick_union import QuickUnion
from union_find.quick_union_waighted import QuickUnionWaighted


class BaseTests():

    def get_instance(self, size=10):
        raise NotImplementedError()

    @property
    def EXPECTED_STRUCTURE(self):
        raise NotImplementedError()

    @pytest.fixture()
    def obj(self):
        obj = self.get_instance()
        obj.union(2, 3)
        obj.union(3, 4)
        obj.union(0, 5)
        obj.union(6, 7)
        obj.union(0, 6)
        return obj

    def test_general(self, obj):

        for a, b in [(0, 1), (1, 0), (1, 8), (7, 8), (7, 1), (4, 5)]:
            error = "%s is connected to %s"
            assert not obj.connected(a, b), error % (a, b)
            assert not obj.connected(b, a), error % (b, a)

        for a, b in [(0, 5), (0, 6), (0, 7), (2, 2), (2, 3), (4, 3)]:
            error = "%s is not connected to %s"
            assert obj.connected(a, b), error % (a, b)
            assert obj.connected(b, a), error % (b, a)

    def test_array_verification(self, obj):
        assert str(obj) == self.EXPECTED_STRUCTURE


class TestQuickFind(BaseTests):

    EXPECTED_STRUCTURE = '         0    1    2    3    4    5    6    7    8\n         0    1    2    2    2    0    0    0    8' # noqa

    def get_instance(self, size=10):
        return QuickFind(size)


class TestQuickUnion(BaseTests):

    EXPECTED_STRUCTURE = '         0    1    2    3    4    5    6    7    8\n         5    1    3    4    4    7    7    7    8' # noqa

    def get_instance(self, size=10):
        return QuickUnion(size)


class TestQuickUnionWaighted(BaseTests):

    EXPECTED_STRUCTURE = '         0    1    2    3    4    5    6    7    8\n         0    1    2    2    2    0    0    6    8' # noqa

    def get_instance(self, size=10):
        return QuickUnionWaighted(size)
