import unittest
from support import save_score, fetch_scores


class TestSupport(unittest.TestCase):
    def setUp(self):
        pass

    def test_points_are_saved_correctly(self):
        points = [1, 2, 3]
        save_score(1)
        save_score(2)
        save_score(3)
        scores = fetch_scores()
        score_list = [scores[-3], scores[-2], scores[-1]]
        self.assertEqual(points, score_list)
        