def euclideanDistance(point1, point2):
    """
  Argümanlar:
    point1: (x1, y1) şeklinde bir demet (tuple) olan ilk nokta.
    point2: (x2, y2) şeklinde bir demet (tuple) olan ikinci nokta.

  Geri dönen değer:
    İki nokta arasındaki Öklid mesafesi.
  """
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def main():
    # Noktaların tanımı
    points = [
        (7, 15),
        (10, 19),
        (7, 1),
        (25, 7)
    ]

    # Mesafelerin hesaplanması ve distances listesine eklenmesi
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)

    # Minimum mesafeyi bulma ve yazdırma
    minDistance = min(distances)
    print("Tüm mesafeler:", distances)
    print("Minimum mesafe:", minDistance)


if __name__ == "__main__":
    main()
