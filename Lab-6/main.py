from __future__ import annotations
import unittest

class Weapon:
    def __init__(self, ammo_capacity: int, fire_rate: int, range_dist: float) -> None:
        self.ammo_capacity = ammo_capacity
        self.fire_rate = fire_rate
        self.range_dist = range_dist
        self._type = None

    def time_to_empty(self) -> float:
        if self.fire_rate == 0:
            return float('inf')
        return self.ammo_capacity / self.fire_rate
    
    def __str__(self) -> str:
        return f'Ammo: {self.ammo_capacity}, FireRate: {self.fire_rate}'

    def __add__(self, other: Weapon) -> Weapon:
        if not isinstance(other, Weapon):
            raise TypeError(f'Невозможно сложить объекти типа Weapon и {type(other)}')
        if self._type == other._type:
            self.ammo_capacity += other.ammo_capacity
            return self
        else:
            raise TypeError(f'Типы оружий не совпадают!\n{self._type} != {other._type}')


class AssaultRiffle(Weapon):
    def __init__(self, ammo_capacity: int, fire_rate: int, range_dist: float, burst_mode: str) -> None:
        super().__init__(ammo_capacity, fire_rate, range_dist)
        self.burst_mode = burst_mode
        self._type = 'AssaultRiffle'

    def __str__(self) -> str:
        return f"{super().__str__()}, BurstMode: {self.burst_mode}"

    def rate_to_range_ratio(self) -> float:
        if self.range_dist == 0:
            return float('inf') if self.fire_rate > 0 else 0
        return self.fire_rate / self.range_dist

class SniperRiffle(Weapon):
    def __init__(self, ammo_capacity: int, fire_rate: int, range_dist: float, zoom_options: tuple[float, ...]) -> None:
        super().__init__(ammo_capacity, fire_rate, range_dist)
        self.zoom_options = zoom_options
        self._type = 'SniperRiifle'

    def __str__(self) -> str:
        return f"{super().__str__()}, ZoomOptions: {self.zoom_options}"

    def rate_to_range_ratio(self) -> float:
        if self.range_dist == 0:
            return float('inf') if self.fire_rate > 0 else 0
        return self.fire_rate / self.range_dist
    
class TestWeapon(unittest.TestCase):
    def test_time_to_empty(self):
        weapon = Weapon(30, 10, 100)
        self.assertEqual(weapon.time_to_empty(), 3.0)

    def test_time_to_empty_zero_fire_rate(self):
        weapon = Weapon(30, 0, 100)
        self.assertEqual(weapon.time_to_empty(), float('inf'))

    def test_add_same_type(self):
        weapon1 = AssaultRiffle(30, 10, 100, "single")
        weapon2 = AssaultRiffle(15, 5, 50, "burst")
        weapon1 += weapon2
        self.assertEqual(weapon1.ammo_capacity, 45)


    def test_add_different_type(self):
        weapon1 = AssaultRiffle(30, 10, 100, "single")
        weapon2 = SniperRiffle(15, 5, 50, (2.5, 5.0))
        with self.assertRaises(TypeError):
            weapon1 += weapon2
    
    def test_add_wrong_type(self):
        weapon1 = AssaultRiffle(30, 10, 100, "single")
        with self.assertRaises(TypeError):
            weapon1 += 5  # Пытаемся сложить с числом


class TestAssaultRiffle(unittest.TestCase):
    def test_rate_to_range_ratio(self):
        rifle = AssaultRiffle(30, 10, 100, "single")
        self.assertAlmostEqual(rifle.rate_to_range_ratio(), 0.1)
    
    def test_rate_to_range_ratio_zero_range(self):
        rifle = AssaultRiffle(30, 10, 0, "single")
        self.assertEqual(rifle.rate_to_range_ratio(), float('inf'))


class TestSniperRiffle(unittest.TestCase):
    def test_rate_to_range_ratio(self):
        rifle = SniperRiffle(5, 1, 500, (5.0, 10.0))
        self.assertAlmostEqual(rifle.rate_to_range_ratio(), 0.002)


    def test_rate_to_range_ratio_zero_range(self):
        rifle = SniperRiffle(30, 10, 0, "single")
        self.assertEqual(rifle.rate_to_range_ratio(), float('inf'))


if __name__ == '__main__':
    unittest.main()