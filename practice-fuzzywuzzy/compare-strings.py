from fuzzywuzzy import fuzz


def compare_strings(string_a="Oi Igor.", string_b="Ola Igor"):
    ratio = fuzz.ratio(string_a.lower(), string_b.lower())
    print(ratio)


def partial_ratio(string_a="New York Giants", string_b="Giants"):
    compare_partial_ratio = fuzz.partial_ratio(string_a.lower(), string_b.lower())
    print(compare_partial_ratio)


partial_ratio()
