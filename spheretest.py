import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(sphere.volume(2) == 33.510321638291124)

    def test_volume2(self):
        assert(sphere.volume(3) == 113.09733552923255)

    def test_volume3(self):
        assert(sphere.volume(5) == 523.5987755982989)

    #surface area tests
    print()
    print("------------------------------------------------------------")
    print("SURFACE AREA TESTS")
    print("------------------------------------------------------------")
    
    def test_surfaceArea1(self):
        assert(sphere.surfaceArea(2) == 50.26548245743669)
    
    def test_surfaceArea2(self):
        assert(sphere.surfaceArea(4) == 201.06192982974676)

    def test_surfaceArea3(self):
        assert(sphere.surfaceArea(6) == 452.3893421169302)

    # #failing test
    # def test_volume3(self):
    #     assert(sphere.volume(10,1000) == ??)


if __name__ == '__main__':
    unittest.main()
