import pytest

from dsa.hash_table import HashTable


def test_hash_table_initialization():
    """Test hash table initializacion"""
    expected_result_data_map_indexes = list(range(7))
    expected_result_data_map_values = [None] * 7
    ht = HashTable()
    result_data_map_keys = []
    result_data_map_values = []
    for k, v in enumerate(ht.data_map):
        result_data_map_keys.append(k)
        result_data_map_values.append(v)
    assert result_data_map_keys == expected_result_data_map_indexes
    assert result_data_map_values == expected_result_data_map_values


def test_hash_table_set_item():
    """Test hash table set item method"""
    expected_result_data_map_indexes = list(range(7))
    expected_result_data_map_values = [None, [['cat', 5]], None, None, None, None, None]
    ht = HashTable()
    ht.set_item('cat', 5)
    result_data_map_keys = []
    result_data_map_values = []
    for k, v in enumerate(ht.data_map):
        result_data_map_keys.append(k)
        result_data_map_values.append(v)
    assert result_data_map_keys == expected_result_data_map_indexes
    assert result_data_map_values == expected_result_data_map_values


def test_hash_table_get_item():
    """Test hash table get item method"""
    expected_result_item = 5
    ht = HashTable()
    ht.set_item('cat', 5)
    result_item = ht.get_item('cat')
    assert result_item == expected_result_item


def test_hash_table_delete_item():
    """Test hash table delete item method"""
    expected_result_deleted_item = ['cat', 5]
    ht = HashTable()
    ht.set_item('cat', 5)
    result_deleted_item = ht.delete_item('cat')
    assert result_deleted_item == expected_result_deleted_item


def test_hash_table_keys():
    """Test hash table keys method"""
    expected_result_keys = ['cat', 'house', 'dog']
    ht = HashTable()
    ht.set_item('cat', 5)
    ht.set_item('dog', 6)
    ht.set_item('house', 7)
    result_keys =  ht.keys()
    assert result_keys == expected_result_keys


def test_hash_table_print():
    """Test hash table print method"""
    expected_result_indexes = list(range(7))
    expected_result_values = [None, [['cat', 5]], None, None, [['house', 7]], None, None]
    ht = HashTable()
    ht.set_item('cat', 5)
    ht.set_item('house', 7)
    ht.print_hash_table()
    # this is what print_hash_table method does
    for k, v in enumerate(ht.data_map):
        assert k == expected_result_indexes[k]
        assert v == expected_result_values[k]
