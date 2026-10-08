# -*- coding: utf-8 -*-
"""
Khasi Traditional Culinary Art, Food Culture & Kitchen Heritage.
Comprehensive documentation of indigenous dishes, fermentation traditions,
mountain ingredients, and earthen utensils of Meghalaya.
"""

from typing import Dict, List, Any, Optional

DISHES: List[Dict[str, Any]] = [
    {
        "name": "Jadoh",
        "category": "Main Rice Dish",
        "ingredients": "Short-grain highland rice, pork meat, ginger, onions, black pepper, turmeric, bay leaves (authentic festive version adds pork blood, 'Jadoh snam')",
        "description": "The crown jewel of Khasi gastronomy. Rice cooked directly in flavorful pork stock with tender meat pieces, aromatic ginger, and spices.",
        "cultural_context": "Centerpiece of weddings, festive gatherings, Sunday family dinners, and daily life in Shillong."
    },
    {
        "name": "Dohkhlieh",
        "category": "Meat Salad / Side Dish",
        "ingredients": "Boiled pork (traditionally from the head/cheeks), crisp finely chopped shallots, minced ginger slivers, fiery bird's eye chilies, salt",
        "description": "Light, refreshing, and clean pork salad celebrated for its balance of tender savory pork and pungent crunch of fresh onions and chilies.",
        "cultural_context": "Staple accompaniment served alongside steaming plates of Jadoh or plain white rice."
    },
    {
        "name": "Dohneiiong",
        "category": "Curry / Gravy Dish",
        "ingredients": "Tender pork cuts, roasted black sesame seeds (Nei-ïong) ground to smooth paste, mustard oil, ginger, garlic, green chilies",
        "description": "Succulent pork braised in an earthy, dark, nutty gravy made from slow-roasted black sesame seeds. Rich, hearty, and aromatic.",
        "cultural_context": "Unique signature dish demonstrating the deep Khasi culinary mastery of sesame seeds."
    },
    {
        "name": "Tungrymbai",
        "category": "Fermented Delicacy",
        "ingredients": "Naturally fermented soybeans, pork belly bits, garlic, ginger paste, crushed black sesame, local chilies",
        "description": "Pungent, deeply savory, umami-rich fermented soybean delicacy slow-cooked in a heavy pan until rich, dark, and thick.",
        "cultural_context": "Quintessential comfort food of the Khasi winter hearth; loved throughout the hills for nutrition and digestion."
    },
    {
        "name": "Ja Stem",
        "category": "Rice Preparation",
        "ingredients": "Highland rice, pure Lakadong heirloom turmeric, bay leaves, light ginger",
        "description": "Fragrant golden rice steamed with high-curcumin Lakadong turmeric, giving it an intoxicating mountain aroma and sunny color.",
        "cultural_context": "Gentle, wholesome rice preparation served with fresh pork curry or vegetable stews."
    },
    {
        "name": "Pumaloi",
        "category": "Steamed Rice Bread",
        "ingredients": "Finely hand-pounded red or white rice powder, hot water",
        "description": "Soft, fluffy, cloud-like steamed rice cake prepared inside a unique terracotta vessel with perforated neck ('Khiew Ranei').",
        "cultural_context": "Traditional breakfast and festive staple served hot with milk tea or red tea."
    },
    {
        "name": "Pukhlein",
        "category": "Sweet Snack / Festive Fritter",
        "ingredients": "Red rice flour, concentrated liquid sugarcane jaggery (Mithai), oil for shallow frying",
        "description": "Golden-brown, crispy festive fritters that puff up when dropped into hot oil; crispy on the edges with a soft, chewy, sweet center.",
        "cultural_context": "Essential sweet treat prepared during Shad Suk Mynsiem, New Year, and hospitality tea times."
    },
    {
        "name": "Tungtap",
        "category": "Chutney / Relish",
        "ingredients": "Charred fermented small hill fish, roasted green chilies, raw onions, wild mint / ginger leaves",
        "description": "Fiery, smoky pounded fish chutney bursting with pungency, providing an electrifying flavor boost to any meal.",
        "cultural_context": "Everyday condiment found in every Khasi village household."
    },
    {
        "name": "Doh Syiar Nei-ïong",
        "category": "Poultry Curry",
        "ingredients": "Country chicken (Syiar shnong), roasted black sesame paste, ginger, onions, mountain spices",
        "description": "Free-range country chicken slow-cooked in a rich roasted black sesame gravy, offering deep herbal richness.",
        "cultural_context": "Honored guest meal and festival specialty."
    },
    {
        "name": "Ja-tyrkhang",
        "category": "Vegetable Dish",
        "ingredients": "Tender young fiddlehead fern fronds foraged from mountain streams, onions, mustard oil, green chilies",
        "description": "Wild organic fiddlehead ferns sautéed lightly with aromatic mountain herbs; crunchy, wholesome, and earthy.",
        "cultural_context": "Showcases the rich foraged wild greens heritage of Khasi cuisine."
    },
    {
        "name": "Putharo",
        "category": "Rice Pancake",
        "ingredients": "Coarsely ground rice flour, water, pinch of salt",
        "description": "Soft, thick flat rice pancake baked between two earthen clay griddles ('Saraw') over embers.",
        "cultural_context": "Beloved evening snack sold at roadside village tea stalls ('Dukan Sha') with Dohkhlieh or black tea."
    },
    {
        "name": "Sohphlang",
        "category": "Seasonal Tuber Snack",
        "ingredients": "Crisp white wild mountain tubers (Flemingia vestita), roasted crushed perilla / sesame seeds",
        "description": "Small round crunchy white tubers gathered in autumn, peeled and eaten raw dipped in ground roasted black sesame seeds with salt.",
        "cultural_context": "Unique indigenous tuber found exclusively in the Khasi hills; rich in natural anthelmintic properties."
    },
    {
        "name": "Lung-siej",
        "category": "Preserved Ingredient",
        "ingredients": "Young bamboo shoots sliced thin and naturally fermented in spring water inside sealed bamboo tubes",
        "description": "Tangy, crisp fermented bamboo shoots that lend a mouth-watering tart savoriness to pork and fish curries.",
        "cultural_context": "Ancient forest preservation technique used throughout Meghalaya."
    },
    {
        "name": "Kwai bad Tympew",
        "category": "Social Communion / Digestive",
        "ingredients": "Fresh sliced areca nut (Kwai), fresh green betel leaf (Tympew), a dab of slaked lime paste (Shun)",
        "description": "The eternal emblem of Khasi hospitality and egalitarian communion. Shared upon meeting, visiting a home, or sealing any conversation.",
        "cultural_context": "Transcends social and economic barriers; rich and poor alike share the exact same Kwai with mutual respect."
    },
    {
        "name": "Sha Saw",
        "category": "Beverage",
        "ingredients": "Highland black tea leaves, mountain spring water, sugar (optional)",
        "description": "Clear amber-red tea served piping hot without milk in small glass tumblers; the lifeblood of social conversation in mountain towns.",
        "cultural_context": "The universal welcome drink of the Khasi hills."
    },
    {
        "name": "Khiew Ranei",
        "category": "Traditional Kitchen Utensil",
        "materials": "Black terracotta clay with perforated upper steamer bowl, crafted in Larnai village (Jaintia Hills)",
        "description": "Traditional double-chamber earthen steaming pot designed specifically to steam Pumaloi rice cakes over boiling water.",
        "cultural_context": "Handcrafted using prehistoric paddle-and-anvil techniques passed down through matrilineal potters."
    },
    {
        "name": "Saraw",
        "category": "Traditional Kitchen Utensil",
        "materials": "Heat-treated unglazed red mountain clay",
        "description": "Pair of concave clay griddle plates used to bake Putharo pancakes over glowing hearth coals without oil.",
        "cultural_context": "Essential kitchen equipment of the traditional Khasi hearth."
    }
]

def list_dishes() -> List[Dict[str, Any]]:
    """Return all documented traditional Khasi culinary entries."""
    return DISHES

def get_dish(name: str) -> Optional[Dict[str, Any]]:
    """Lookup dish or culinary preparation by name."""
    q = name.lower().strip()
    for d in DISHES:
        if q in d["name"].lower() or q in d["description"].lower() or q in d["category"].lower():
            return d
    return None

def by_category(cat: str) -> List[Dict[str, Any]]:
    """Filter dishes by culinary category."""
    c = cat.lower().strip()
    return [d for d in DISHES if c in d["category"].lower()]
