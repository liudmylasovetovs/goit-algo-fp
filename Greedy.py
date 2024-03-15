def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, values in sorted_items:
        if total_cost + values["cost"] <= budget:
            total_cost += values["cost"]
            total_calories += values["calories"]
            chosen_items.append(item)

    return {"chosen_items": chosen_items, "total_cost": total_cost, "total_calories": total_calories}


def dynamic_programming(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item, values) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if values["cost"] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - values["cost"]] + values["calories"])

    chosen_items = []
    j = budget
    for i in range(len(items), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    chosen_items.reverse()
    return {"chosen_items": chosen_items, "total_cost": sum(items[item]["cost"] for item in chosen_items),
            "total_calories": dp[len(items)][budget]}


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Chosen items:", greedy_result["chosen_items"])
print("Total cost:", greedy_result["total_cost"])
print("Total calories:", greedy_result["total_calories"])

dp_result = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Chosen items:", dp_result["chosen_items"])
print("Total cost:", dp_result["total_cost"])
print("Total calories:", dp_result["total_calories"])