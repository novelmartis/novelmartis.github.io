import unittest
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
SITE_ORIGIN = "https://www.sushrutthorat.com"


class SiteStructureTests(unittest.TestCase):
    def test_contact_fields_are_required(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('<input name="name" autocomplete="name" required>', page)
        self.assertIn(
            '<input name="email" type="email" autocomplete="email" required>',
            page,
        )
        self.assertIn('<textarea name="message" rows="4" required>', page)

    def test_jee_page_is_linked_from_teaching(self):
        teaching = (ROOT / "portfolio/content/teaching.md").read_text(encoding="utf-8")
        self.assertIn("[Page](./jee_prep/)", teaching)
        self.assertTrue((ROOT / "portfolio/jee_prep/index.html").is_file())

    def test_jee_page_is_hidden_with_the_portfolio(self):
        page = (ROOT / "portfolio/jee_prep/index.html").read_text(encoding="utf-8")
        self.assertIn('<meta name="robots" content="noindex, nofollow">', page)
        self.assertIn(
            '<link rel="canonical" href="https://www.sushrutthorat.com/portfolio/jee_prep/">',
            page,
        )

        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("Disallow: /portfolio/", robots)

    def test_sitemap_covers_public_pages_and_is_advertised(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn(f"Sitemap: {SITE_ORIGIN}/sitemap.xml", robots)

        sitemap = ElementTree.parse(ROOT / "sitemap.xml")
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = {
            element.text for element in sitemap.findall("sm:url/sm:loc", namespace)
        }
        self.assertEqual(
            locations,
            {f"{SITE_ORIGIN}/"},
        )


if __name__ == "__main__":
    unittest.main()
