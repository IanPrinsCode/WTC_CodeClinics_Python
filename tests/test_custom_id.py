import unittest
import custom_id.custom_id as custom_id


class MyTestCase(unittest.TestCase):
    def test_create_custom_id(self):
        id_map = {'c6r':'9p62r8voemob7at56g75rdlqbk'}
        new_id_map = custom_id.create_custom_id(id_map)
        self.assertEqual(type(new_id_map), str)
        self.assertEqual(len(new_id_map), 3)

    def test_update_id_map(self):
        events = {'items':[{'description':'a1b','id':'9p62r8voemob7at56g75rdlqbk'}]}
        response = custom_id.update_id_map(events, {})
        self.assertEqual(response, {'a1b':'9p62r8voemob7at56g75rdlqbk'})

    def test_update_id_map_with_full_map(self):
        events = {'items':[{'description':'a1b','id':'9p62r8voemob7at56g75rdlqbk'}]}
        response = custom_id.update_id_map(events, {'b1a':'9p62r8voemob7at56g75rdlqba'})
        self.assertEqual(response, {'a1b':'9p62r8voemob7at56g75rdlqbk','b1a':'9p62r8voemob7at56g75rdlqba'})

if __name__ == '__main__':
    unittest.main
