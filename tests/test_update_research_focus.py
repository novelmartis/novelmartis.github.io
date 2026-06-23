import unittest

import update_research_focus as urf


class UpdateResearchFocusTests(unittest.TestCase):
    def test_concise_label_trims_topic_suffixes(self) -> None:
        self.assertEqual(
            urf.concise_label("visual perception and processing mechanisms"),
            "visual perception",
        )
        self.assertEqual(
            urf.concise_label("neural dynamics and brain function"),
            "neural dynamics",
        )

    def test_candidate_phrases_prefers_fuller_trigram(self) -> None:
        phrases = urf.candidate_phrases(
            "Predictive remapping in recurrent neural network models of active vision"
        )
        self.assertIn("recurrent neural network", phrases)
        self.assertNotIn("recurrent neural", phrases)

    def test_build_payload_like_summary_joins_two_themes_cleanly(self) -> None:
        author = {"topics": []}
        works = []
        summary, _themes = urf.summarize(author, works)
        self.assertIn("visual search", summary)

    def test_confidence_labels(self) -> None:
        self.assertEqual(urf.confidence_label(0.95), "high")
        self.assertEqual(urf.confidence_label(0.75), "medium")
        self.assertEqual(urf.confidence_label(0.2), "low")


if __name__ == "__main__":
    unittest.main()
