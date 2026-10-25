from models import Customer, FoodItem, Menu, Order


# Build a brand-new sample menu, so tests never share objects.
def make_sample_menu():
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 10.00, "Burgers", 4.2))
    menu.add_item(FoodItem("Large Soda", 5.00, "Drinks", 4.8))
    menu.add_item(FoodItem("Bottled Water", 2.00, "Drinks", 3.0))
    menu.add_item(FoodItem("Chocolate Cake", 4.00, "Desserts", 3.9))
    return menu


# Test that a $10 burger and a $5 soda have a total of $15.
def test_order_total_adds_burger_and_soda():
    order = Order(Customer("Jose"))
    order.add_item(FoodItem("Spicy Burger", 10.00, "Burgers", 4.2))
    order.add_item(FoodItem("Large Soda", 5.00, "Drinks", 4.8))
    assert order.compute_total() == 15


# Test that an empty order has a total of 0.
def test_empty_order_total_is_zero():
    order = Order(Customer("Jose"))
    assert order.compute_total() == 0


# Test that filtering "Drinks" returns only drink items.
def test_filter_drinks_returns_only_drinks():
    menu = make_sample_menu()
    drink_names = [item.name for item in menu.filter_by_category("Drinks")]
    assert sorted(drink_names) == ["Bottled Water", "Large Soda"]


# Test that filtering a missing category returns an empty list.
def test_filter_with_no_matches_returns_empty_list():
    menu = make_sample_menu()
    assert menu.filter_by_category("Salads") == []


# Test that "drinks" does not match the category "Drinks".
def test_filter_is_case_sensitive():
    menu = make_sample_menu()
    assert menu.filter_by_category("drinks") == []


# Test that sorting puts the highest popularity first
# without changing the original menu order.
def test_sort_by_popularity_highest_first_and_menu_unchanged():
    menu = make_sample_menu()
    sorted_names = [item.name for item in menu.sort_by_popularity()]
    menu_names = [item.name for item in menu.items]
    assert sorted_names == ["Large Soda", "Spicy Burger", "Chocolate Cake", "Bottled Water"]
    assert menu_names == ["Spicy Burger", "Large Soda", "Bottled Water", "Chocolate Cake"]


# Test that adding the same soda twice counts its price twice.
def test_same_item_twice_counts_price_twice():
    order = Order(Customer("Jose"))
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.8)
    order.add_item(soda)
    order.add_item(soda)
    assert order.compute_total() == 10
