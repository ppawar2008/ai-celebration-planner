
import unittest

from planner_utils import calculate_budget, get_demo_ideas


class TestBudget(unittest.TestCase):

    def test_budget_allocation(self):
        result = calculate_budget(10000)

        self.assertAlmostEqual(result["Venue"], 3000)
        self.assertAlmostEqual(result["Food & Drinks"], 3500)
        self.assertAlmostEqual(result["Decorations"], 2000)
        self.assertAlmostEqual(result["Other"], 1500)

    def test_invalid_budget(self):
        with self.assertRaises(ValueError):
            calculate_budget(100)

    def test_budget_type(self):
        with self.assertRaises(TypeError):
            calculate_budget("10000")

    def test_nan_budget(self):
        with self.assertRaises(ValueError):
            calculate_budget(float("nan"))

    def test_infinite_budget(self):
        with self.assertRaises(ValueError):
            calculate_budget(float("inf"))

    def test_boolean_budget(self):
        with self.assertRaises(TypeError):
            calculate_budget(True)


class TestEventIdeas(unittest.TestCase):

    def test_birthday_ideas(self):
        result = get_demo_ideas(
            "Birthday Party", "Elegant", 30, ""
        )

        self.assertGreaterEqual(len(result), 4)
        self.assertTrue(
            any("photo" in idea.lower() for idea in result)
        )

    def test_special_request(self):
        result = get_demo_ideas(
            "Birthday Party", "Elegant", 30, "Music"
        )

        self.assertTrue(any("Music" in idea for idea in result))

    def test_unknown_event(self):
        result = get_demo_ideas(
            "Unknown Event", "Minimal", 20, ""
        )

        self.assertGreaterEqual(len(result), 4)

    def test_invalid_guest_count(self):
        with self.assertRaises(ValueError):
            get_demo_ideas("Birthday Party", "Elegant", 0, "")

    def test_theme_is_used(self):
        result = get_demo_ideas(
            "Birthday Party", "Retro", 30, ""
        )

        self.assertTrue(any("Retro" in idea for idea in result))


if __name__ == "__main__":
    unittest.main()
