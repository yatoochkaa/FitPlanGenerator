import random


def generate_workout(exercises, count=4):
    selected = random.sample(exercises, count)
    return selected


if __name__ == "__main__":
    exercises = [
        "Приседания",
        "Отжимания",
        "Планка",
        "Выпады",
        "Подтягивания"
    ]

    workout = generate_workout(exercises)

    print("Ваша тренировка:")
    for exercise in workout:
        print("-", exercise)