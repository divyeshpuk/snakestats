import unittest
import snakestats


class TestsForSnakeStats(unittest.TestCase):
    # SET 1
    # Target function name: calc_mean_num_of_mixed_vals_list
    def test_calc_mean_num_of_mixed_vals_list_1_val(self):
        # ARRANGE
        nums = [1]
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(mean_num, 1.0)

    def test_calc_mean_num_of_mixed_vals_list_2_vals(self):
        # ARRANGE
        nums = [1, 2]
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(mean_num, 1.5)

    def test_calc_mean_num_of_mixed_vals_list_3_vals(self):
        # ARRANGE
        nums = [1, 2, 3]
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(mean_num, 2.0)

    def test_calc_mean_num_of_mixed_vals_list_empty(self):
        # ARRANGE
        empty = []
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(empty)
        # ASSERT
        self.assertEqual(mean_num, None)

    def test_calc_mean_num_of_mixed_vals_list_is_not_list(self):
        # ARRANGE
        # Can be any data type
        not_list = None
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(not_list)
        # ASSERT
        self.assertEqual(mean_num, None)

    def test_calc_mean_num_of_mixed_vals_list_mult(self):
        # ARRANGE
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(mean_num, 8.0)

    def test_calc_mean_num_of_mixed_vals_list_str(self):
        # ARRANGE
        vals = ["foo", "bar"]
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(vals)
        # ASSERT
        self.assertEqual(mean_num, None)

    def test_calc_mean_num_of_mixed_vals_list_mixed(self):
        # ARRANGE
        vals = [1, "foo", "bar", 2, None, ["a", "b", "c"], ("a", "b", "c"), True, {"a": "b"}]
        # ACT
        mean_num = snakestats.calc_mean_num_of_mixed_vals_list(vals)
        # ASSERT
        self.assertEqual(mean_num, 1.5)

    # SET 2
    # Target function name: get_max_num_in_mixed_vals_list
    def test_get_max_num_in_mixed_vals_list_first_index(self):
        # ARRANGE
        nums = [6]
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(max_num, 6)

    def test_get_max_num_in_mixed_vals_list_last_index(self):
        # ARRANGE
        nums = [6, 7]
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(max_num, 7)

    def test_get_max_num_in_mixed_vals_list_any_index(self):
        # ARRANGE
        nums = [6, 5, 4, 7, 2, 3]
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(max_num, 7)

    def test_get_max_num_in_mixed_vals_list_empty(self):
        # ARRANGE
        empty = []
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(empty)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_max_num_in_mixed_vals_list_is_not_list(self):
        # ARRANGE
        # Can be any data type
        not_list = None
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(not_list)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_max_num_in_mixed_vals_list_neg(self):
        # ARRANGE
        nums = [-6, -5, -4, -3, -2, -7]
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(max_num, -2)

    def test_get_max_num_in_mixed_vals_list_str(self):
        # ARRANGE
        vals = ["a", "b", "c"]
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(vals)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_max_num_in_mixed_vals_list_mixed(self):
        # ARRANGE
        vals = ["6", -5, -4, "abc", -3, -2, -7.5, None, "123", -4.78, 7.001, 7.0, 5, "foo", -9, ["a", "b"], ("a", "b"), True, {"a": "b"}]
        # ACT
        max_num = snakestats.get_max_num_in_mixed_vals_list(vals)
        # ASSERT
        self.assertEqual(max_num, 7.001)

    # SET 3
    # Target function name: get_mode_num_in_mixed_vals_list
    def test_get_mode_num_in_mixed_vals_list_1_num(self):
        # ARRANGE
        nums = [1]
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(max_num, 1)

    def test_get_mode_num_in_mixed_vals_list_nums(self):
        # ARRANGE
        nums = [1, 1, 2, 2, 3, 2, 2]
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(nums)
        # ASSERT
        self.assertEqual(max_num, 2)

    def test_get_mode_num_in_mixed_vals_list_empty(self):
        # ARRANGE
        empty = []
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(empty)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_mode_num_in_mixed_vals_list_is_not_list(self):
        # ARRANGE
        # Can be any data type
        not_list = None
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(not_list)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_mode_num_in_mixed_vals_list_none(self):
        # ARRANGE
        all_none = [None, None]
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(all_none)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_mode_num_in_mixed_vals_list_str(self):
        # ARRANGE
        vals = ["a", "b", "c"]
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(vals)
        # ASSERT
        self.assertEqual(max_num, None)

    def test_get_mode_num_in_mixed_vals_list_mixed(self):
        # ARRANGE
        vals = ["foo", -5, -4, "abc", -3, -2, -7.5, None, 5, "123", -4.78, 7.001, 7.0, 5, "bar", -9, 5, ["a", "b"], ("a", "b"), True, {"a": "b"}]
        # ACT
        max_num = snakestats.get_mode_num_in_mixed_vals_list(vals)
        # ASSERT
        self.assertEqual(max_num, 5)


unittest.main(argv=['ignored', '-v'], exit=False)
