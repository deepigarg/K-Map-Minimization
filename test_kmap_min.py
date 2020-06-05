# Name: DEEPI GARG
# Roll Number: 2018389
# Section: B
# Group: 6
# Date: 12-10-2018

import unittest
from kmap_min import minFunc



class testpoint(unittest.TestCase):
        def test_minFunc(self):
                self.assertEqual(minFunc(4,"(1,3,7,11,15)d(0,2,5)"),"W'X'+YZ")
                self.assertEqual(minFunc(4,"(0,1,2,4,5,6,8,9,12,13,14)d-"),"W'Z'+XZ'+Y'")
                self.assertEqual(minFunc(4,"()d(1,14,2)"),0)
                self.assertEqual(minFunc(3,"(0,1,2,6,7)d(3,4,5)"),1)
                self.assertEqual(minFunc(4,"(0,8,10,12,13,14)d(2,15)"),"WX+X'Z'")
                self.assertEqual(minFunc(4,"(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)d()"),1)
                self.assertEqual(minFunc(4,"(1,3,5,4)d(2,10)"),"W'X'Z+W'XY'")
                self.assertEqual(minFunc(3,"(0,1,2,7,5)d-"),"W'X'+W'Y'+WY")
                self.assertEqual(minFunc(3,"(2,4)d(0,6)"),"Y'")
                self.assertEqual(minFunc(4,"(1,4,6,13,14,9)d(15,2)"),"W'XZ'+WY'Z+X'Y'Z+XYZ'")
                self.assertEqual(minFunc(4,"(0,1,2,3,4,5,7)d(10,11,15)"),"W'X'+W'Y'+YZ")
                self.assertEqual(minFunc(3,"(0,2,5,6)d(7)"),"W'Y'+WY+XY'")
                self.assertEqual(minFunc(4,"(0,1,3,4,5,7)d(2,10,11,15)"),"W'Y'+W'Z")
                self.assertEqual(minFunc(3,"(3,6,4)d-"),"W'XY+WY'")
                self.assertEqual(minFunc(4,"(0,2,5,15,8,10)d-"),"W'XY'Z+WXYZ+X'Z'")
                self.assertEqual(minFunc(4,"(0,8,10,12,13,14,11)d(9,2,15)"),"W+X'Z'")
                self.assertEqual(minFunc(2,"()d(0,1,2,3)"),0)
                self.assertEqual(minFunc(2,"(0,3)d(2,1)"),1)
                self.assertEqual(minFunc(2,"(1,2)d(3)"),"W+X")
                self.assertEqual(minFunc(2,"(0,2)d(3)"),"X'")
                self.assertEqual(minFunc(3,"(1,3,2,4,6)d(0,5)"),"W'+Y'")
                self.assertEqual(minFunc(4,"(1,4,5,7,6,13,14,9,11,10)d(3,2,15,12,8)"),"X+Y+Z")
                
                
if __name__=='__main__' :
        unittest.main()
