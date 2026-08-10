def calculate_bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("Height must be greater than zero")

    return weight_kg / (height_m ** 2)


if __name__ == "__main__":
    bmi = calculate_bmi(70, 1.75)
    print("BMI:", round(bmi, 2))
